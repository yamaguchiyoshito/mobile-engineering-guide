"""Check that every external https link in the documents is reachable. Run manually or on a schedule."""
from common import *
import sys,urllib.request,urllib.error,concurrent.futures
urls=set()
for p in PAGES:
 for url in re.findall(r'\]\((https://(?:[^()\s]|\([^()\s]*\))+)\)',without_code(body(p['path']))):urls.add(url.rstrip('.'))
def probe(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (documentation link check)'},method='GET')
 try:
  with urllib.request.urlopen(req,timeout=30) as r:return url,r.status
 except urllib.error.HTTPError as e:return url,e.code
 except Exception as e:return url,type(e).__name__
with concurrent.futures.ThreadPoolExecutor(8) as ex:results=list(ex.map(probe,sorted(urls)))
failed=[(u,s) for u,s in results if s!=200]
for u,s in failed:print(f'{s} {u}')
print(f'Links checked: {len(urls)}; unreachable: {len(failed)}')
sys.exit(1 if failed else 0)
