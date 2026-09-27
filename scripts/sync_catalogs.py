"""Keep GitHub-readable catalog blocks aligned with the single document map."""
from common import *
import sys

def catalog(page):
 path=page['path'];kind=page['kind'];out=[]
 if kind=='skill-index':
  out=['| 領域 | 要素技術数 |','| :--- | :---: |']
  for area in MAP['areas']:
   target=f'skills/{area["id"]}/index.md';count=sum(p['kind']=='skill' and p['area']==area['id'] for p in PAGES)
   out.append(f'| [{area["title"]}]({rel(path,target)}) | {count} |')
 elif kind=='area':
  out=['| 要素技術ID | 要素技術 | 対象 | 評価対象・主な前提 |','| :--- | :--- | :--- | :--- |']
  for p in PAGES:
   if p['kind']=='skill' and p['area']==page['area']:
    text=body(p['path']);prerequisite=re.search(r'\*\*(?:評価対象|主な前提)：\*\* (.+)',text).group(1).strip()
    platform=re.search(r'\*\*対象プラットフォーム：\*\* (.+)',text).group(1).strip()
    out.append(f'| `{p["skillId"]}` | [{p["title"]}]({rel(path,p["path"])}) | {platform} | {prerequisite} |')
 elif kind=='checklist-index':
  section=None
  for p in PAGES:
   if p['kind']!='checklist':continue
   if section!=p['section']:
    section=p['section'];out += ['','## '+section,'','| 項目No. | 分野 |','| :--- | :--- |']
   out.append(f'| {p["numbers"][0]}〜{p["numbers"][-1]} | [{p["title"]}]({rel(path,p["path"])}) |')
 elif kind=='template-index':
  out=[f'- [{p["title"]}]({rel(path,p["path"])})' for p in PAGES if p['kind']=='template']
 elif page.get('learning')=='index':
  out=['| 段階 | 目的 | 到達目安 |','| :--- | :--- | :--- |']
  for i,s in enumerate(LEARNING['stages'],1):out.append(f"| {i}.{s['title']} | {s['goal']} | {s['target']} |")
  for pl in LEARNING['platforms']:
   out+=['',f"## {pl['title']}",'','| 段階 | 学ぶ要素技術 |','| :--- | :--- |']
   for i,s in enumerate(pl['stages'],1):
    links='、'.join(f"[{SKILLS_BY_ID[i2]['title']}]({rel(path,SKILLS_BY_ID[i2]['path'])})" for i2 in s['skills'])
    out.append(f"| {i}.{s['title']} | {links} |")
   out+=['',pl['note'],'',f"課題と学習資料を段階順にまとめた[学習コンテンツ：{pl['title']}]({rel(path,pl['path'])})を参照してください。"]
 else:return None
 return '\n'.join(out).strip()

def references_table(ids):
 order={k:i for i,k in enumerate(REF_TYPES)}
 rows=sorted((REFS[i] for i in ids),key=lambda r:(order[r['type']],min(PLATFORM_ORDER.index(x) for x in r['platforms'])))
 out=['| 種別 | 名称 | 対象 | 概要 |','| :--- | :--- | :--- | :--- |']
 for r in rows:out.append(f"| {REF_TYPES[r['type']]} | [{r['title']}]({r['url']}) | {'・'.join(r['platforms'])} | {r['summary']} |")
 return '\n'.join(out)

def learning_block(page):
 pl=next(p for p in LEARNING['platforms'] if p['id']==page['learning']);path=page['path'];out=[]
 for i,s in enumerate(pl['stages'],1):
  out+=[f"## 段階{i}：{s['title']}",'',f"{s['goal']}到達目安は{s['target']}です。",'']
  for sid in s['skills']:
   sp=SKILLS_BY_ID[sid];plat=skill_platform(sp);extra='' if plat in ('共通',pl['id']) else '（必要に応じて）'
   out+=[f"### {sp['title']}{extra}",'',f"{about_sentence(sp)}詳しくは[{sp['title']}のページ]({rel(path,sp['path'])})を参照してください。",'','| 目標 | 取り組む課題の例 | 参考資料 |','| :--- | :--- | :--- |']
   for lv,task,refs in task_rows(sp):out.append(f'| {lv} | {task} | {refs} |')
   learn=[REFS[i2] for i2 in (reference_ids(body(sp['path'])) or []) if REFS[i2]['type']=='learning' and set(REFS[i2]['platforms'])&{'共通',pl['id']}]
   if learn:out+=['','学習資料：'+'・'.join(f"[{r['title']}]({r['url']})" for r in learn)]
   out.append('')
 return '\n'.join(out).rstrip()

def sync(check=False):
 dirty=[]
 for page in PAGES:
  file=DOCS/page['path'];text=file.read_text()
  if page.get('learning') and page['learning']!='index':
   if '<!-- learning:start -->' not in text:raise ValueError(f'{file}: learning block missing')
   new=re.sub(r'<!-- learning:start -->.*?<!-- learning:end -->',lambda m:f'<!-- learning:start -->\n\n{learning_block(page)}\n\n<!-- learning:end -->',text,flags=re.S)
   if new!=text:
    dirty.append(page['path'])
    if not check:file.write_text(new)
    text=new
  if page['kind']=='skill' or reference_ids(text) is not None:
   ids=reference_ids(text)
   if ids is None:raise ValueError(f'{file}: references block missing')
   missing=[i for i in ids if i not in REFS]
   if missing:raise ValueError(f'{file}: unknown reference ids: {", ".join(missing)}')
   new=re.sub(r'(<!-- references:start ids="[^"]*" -->).*?(<!-- references:end -->)',lambda m:f'{m.group(1)}\n\n{references_table(ids)}\n\n{m.group(2)}',text,flags=re.S)
   if new!=text:
    dirty.append(page['path'])
    if not check:file.write_text(new)
    text=new
  value=catalog(page)
  if value is None:continue
  new,count=re.subn(r'<!-- catalog:start -->.*?<!-- catalog:end -->',f'<!-- catalog:start -->\n\n{value}\n\n<!-- catalog:end -->',text,flags=re.S)
  if count!=1:raise ValueError(f'{file}: catalog markers missing or duplicated')
  if new!=text:
   dirty.append(page['path'])
   if not check:file.write_text(new)
 if check and dirty:raise ValueError('Run npm run docs:sync: '+', '.join(dirty))
 return dirty
if __name__=='__main__':
 try:print('Catalogs checked' if '--check' in sys.argv else 'Catalogs synchronized:',len(sync('--check' in sys.argv)))
 except ValueError as e:sys.exit(str(e))
