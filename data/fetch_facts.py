# Faits par commune depuis Wikipédia FR : intro (texte rendu) + infobox (altitude, superficie, site web, localités, gentilé, voisines).
import json,re,urllib.request,urllib.parse,time,html,sys
UA={'User-Agent':'arboritaille-site builder (contact@arboritaille.ch)'}
def api(params):
    url='https://fr.wikipedia.org/w/api.php?'+urllib.parse.urlencode(dict(params,format='json'))
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60))
        except Exception as e:
            if i==2: raise
            time.sleep(2)
def strip(s): return html.unescape(re.sub(r'<[^>]+>','',s)).replace('\xa0',' ').strip()
communes=json.load(open('communes_zone.json'))
facts={}
try: facts=json.load(open('communes_faits.json'))
except: pass
for i,c in enumerate(communes):
    if c['page'] in facts: continue
    try:
        p=api({'action':'parse','page':c['page'],'prop':'text|sections','redirects':1})['parse']
    except Exception as e:
        print('ERR',c['page'],e,file=sys.stderr); continue
    h=p['text']['*']
    # infobox
    ib={}
    m=re.search(r'<table class="infobox[^"]*".*?</table>',h,flags=re.S)
    if m:
        for row in re.findall(r'<tr[^>]*>(.*?)</tr>',m.group(0),flags=re.S):
            th=re.search(r'<th[^>]*>(.*?)</th>',row,flags=re.S); td=re.search(r'<td[^>]*>(.*?)</td>',row,flags=re.S)
            if th and td:
                k=strip(th.group(1)); v=strip(td.group(1))
                if k and v and len(v)<400: ib[k]=v
        web=re.search(r'<a [^>]*href="(https?://[^"]+)"[^>]*class="external',m.group(0))
        if web: ib['_site_web']=web.group(1)
    # intro : paragraphes avant le premier h2
    body=h.split('<h2',1)[0]
    paras=[strip(x) for x in re.findall(r'<p>(.*?)</p>',body,flags=re.S)]
    intro=' '.join(x for x in paras if len(x)>40)[:2500]
    # sections géographie / toponymie / patrimoine / histoire (titres + 1er paragraphe)
    secs={}
    for t in ['Géographie','Toponymie','Histoire','Patrimoine','Économie','Monuments','Culture et patrimoine','Localités','Transports','Climat']:
        mm=re.search(r'<h2[^>]*>(?:<span[^>]*>)*\s*'+re.escape(t)+r'.*?</h2>(.*?)(?=<h2|\Z)',h,flags=re.S)
        if mm:
            ps=[strip(x) for x in re.findall(r'<p>(.*?)</p>',mm.group(1),flags=re.S) if len(strip(x))>40]
            lis=[strip(x) for x in re.findall(r'<li>(.*?)</li>',mm.group(1),flags=re.S)][:12]
            if ps or lis: secs[t]={'p':' '.join(ps)[:1800],'li':[x[:120] for x in lis]}
    facts[c['page']]={'infobox':ib,'intro':intro,'sections':secs}
    if i%10==0:
        json.dump(facts,open('communes_faits.json','w'),ensure_ascii=False)
        print(i,'/',len(communes),c['page'],file=sys.stderr)
    time.sleep(0.25)
json.dump(facts,open('communes_faits.json','w'),ensure_ascii=False)
print('done',len(facts))
