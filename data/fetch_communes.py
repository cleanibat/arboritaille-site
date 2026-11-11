# Récupère les communes de la zone depuis Wikipédia FR (tableaux rendus) puis les faits de chaque commune (infobox + intro).
import json,re,urllib.request,urllib.parse,time,html,sys
UA={'User-Agent':'arboritaille-site builder (contact@arboritaille.ch)'}
def api(params):
    url='https://fr.wikipedia.org/w/api.php?'+urllib.parse.urlencode(dict(params,format='json'))
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60))
        except Exception as e:
            if i==2: raise
            time.sleep(2)
def rendered(title): return api({'action':'parse','page':title,'prop':'text','redirects':1})['parse']['text']['*']
def strip(s): return html.unescape(re.sub(r'<[^>]+>','',s)).replace('\xa0',' ').strip()
def num(s):
    s=re.sub(r'[^\d]','',s); return int(s) if s else None
LISTS={'JU':'Liste des communes du canton du Jura','NE':'Communes du canton de Neuchâtel','FR':'Communes du canton de Fribourg','VD':'Communes du canton de Vaud','BE':'Arrondissement administratif du Jura bernois','BE2':'Arrondissement administratif de Bienne'}
communes=[]
for canton,title in LISTS.items():
    h=rendered(title)
    tables=re.findall(r'<table class="wikitable[^"]*".*?</table>',h,flags=re.S)
    tbl=max(tables,key=len) if tables else ''
    rows=re.findall(r'<tr[^>]*>(.*?)</tr>',tbl,flags=re.S)
    hdr=[strip(c) for c in re.findall(r'<th[^>]*>(.*?)</th>',rows[0],flags=re.S)] if rows else []
    for r in rows[1:]:
        cells=re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',r,flags=re.S)
        if len(cells)<3: continue
        m=re.search(r'<a href="/wiki/([^"#]+)"[^>]*>([^<]+)</a>',cells[0])
        if not m: continue
        page=urllib.parse.unquote(m.group(1)).replace('_',' '); name=strip(m.group(2))
        vals=[strip(c) for c in cells]
        d={'canton':canton[:2],'nom':name,'page':page,'cellules':vals}
        # colonnes selon la liste
        low=[x.lower() for x in hdr]
        def col(key):
            for i,hh in enumerate(low):
                if key in hh and i<len(vals): return vals[i]
            return None
        d['ofs']=num(col('ofs') or '')
        d['district']=col('district') or col('région') or col('arrondissement') or None
        d['population']=num(col('population') or '')
        d['superficie']=col('superficie')
        communes.append(d)
    print(canton,len([c for c in communes if c['canton']==canton[:2]]),'communes cumulées',file=sys.stderr)
json.dump(communes,open('communes_listes.json','w'),ensure_ascii=False,indent=1)
print(len(communes),'communes au total')
