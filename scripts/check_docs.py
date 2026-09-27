"""Validate catalog completeness, stable IDs, criterion polarity and source links."""
from common import *
from sync_catalogs import sync
import sys,hashlib
PLATFORMS=['共通','iOS','Android','React Native']

def main():
 sync(check=True)
 files={str(p.relative_to(DOCS)) for p in DOCS.rglob('*.md') if '.vitepress' not in p.parts and 'public' not in p.parts}
 paths=[p['path'] for p in PAGES]
 assert len(paths)==len(set(paths)),'Duplicate page paths'
 assert files==set(paths),f'Unmapped/missing Markdown: {files.symmetric_difference(paths)}'
 assert len(paths)==89,'Initial release must contain 89 pages'
 skills=[p for p in PAGES if p['kind']=='skill'];checks=[p for p in PAGES if p['kind']=='checklist']
 assert len(skills)==34 and len(checks)==25,'Expected 34 skills and 25 checklist groups'
 assert len({p['skillId'] for p in skills})==34,'Duplicate skill ID'
 assert len({p['area'] for p in skills})==4,'Expected four skill areas'
 definitions={};items={}
 for p in skills:
  ds=definition_data(p)
  platform=re.search(r'^\*\*対象プラットフォーム：\*\* (.+)$',body(p['path']),re.M)
  assert platform and platform.group(1).strip() in PLATFORMS,p['path']+': platform line must be one of '+', '.join(PLATFORMS)
  assert list(ds)==['Lv0','Lv1','Lv2','Lv3','Lv4'],p['path']+': five definitions required'
  for lv,text in ds.items():
   assert text.strip(),p['path']+': empty definition'
   definitions[p['skillId']+'.'+lv]=hashlib.sha256(text.encode()).hexdigest()
 for p in checks:
  rows=checklist_data(p);assert list(rows)==p['numbers'],p['path']+': item numbers differ'
  for num,row in rows.items():
   assert num not in items,'Duplicate checklist number'
   assert row[2]==('FALSE' if int(num)%4==0 else 'TRUE'),f'C{num}: expected polarity changed; revise the validation rule only with a criteria change'
   items[num]=hashlib.sha256(json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
 assert list(items)==[f'{n:03}' for n in range(1,101)],'100 sequential items required'
 used=set()
 for p in skills:
  ids=reference_ids(body(p['path']))
  assert ids and 3<=len(ids)<=15,p['path']+': 3 to 15 references required'
  assert len(ids)==len(set(ids)),p['path']+': duplicate reference id'
  used.update(ids)
 learning_pages=[p for p in PAGES if p.get('learning') and p['learning']!='index']
 assert [p['learning'] for p in learning_pages]==[pl['id'] for pl in LEARNING['platforms']],'Learning pages must match learning-paths.json platforms'
 for p,pl in zip(learning_pages,LEARNING['platforms']):
  assert p['path']==pl['path'],p['path']+': learning path mismatch'
  ids=reference_ids(body(p['path']));assert ids and len(ids)==len(set(ids)),p['path']+': course references required'
  used.update(ids)
  listed=[s for st in pl['stages'] for s in st['skills']]
  assert len(listed)==len(set(listed)),pl['id']+': skill listed twice'
  assert set(listed)<=set(SKILLS_BY_ID),pl['id']+': unknown skill id'
  required={sid for sid,sp in SKILLS_BY_ID.items() if skill_platform(sp) in ('共通',pl['id'])}
  assert required<=set(listed),pl['id']+': missing skills '+', '.join(sorted(required-set(listed)))
  for sid in listed:assert len(task_rows(SKILLS_BY_ID[sid]))==3,sid+': three task rows required'
 assert len(REFS)==len(REFERENCES['references']),'Duplicate reference id in registry'
 unused=set(REFS)-used
 assert not unused,'Unused references: '+', '.join(sorted(unused))
 for r in REFERENCES['references']:
  assert r['url'].startswith('https://') and r['type'] in REF_TYPES and r['platforms'] and set(r['platforms'])<=set(PLATFORM_ORDER),r['id']+': invalid reference record'
  assert 0<len(r['summary'])<=60,r['id']+': summary must be 1 to 60 characters'
 for p in PAGES:
  text=without_code(body(p['path']))
  assert re.findall(r'^# (.+)$',text,re.M)==[p['title']],p['path']+': page title differs from document map'
  assert not re.search(r'(スキル階層|レベル[1-4][：:]|第[2-7]章|付録[AB]|フロントエンド開発ガイド(?!\]))',text),p['path']+': obsolete reference or area term'
  for url in re.findall(r'\]\(([^)]+)\)',text):
   if re.match(r'^(https?://|mailto:|#)',url):continue
   target=url.split('#')[0]
   assert not target.startswith('/'),f'{p["path"]}: use relative Markdown links: {url}'
   assert (DOCS/p['path']).parent.joinpath(target).exists(),f'{p["path"]}: broken link {url}'
 print(f'Docs OK: {len(paths)} pages, {len(definitions)} definitions, {len(items)} items (75 TRUE / 25 FALSE), {len(REFS)} references')
if __name__=='__main__':
 try:main()
 except (AssertionError,ValueError) as e:sys.exit(str(e))
