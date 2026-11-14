# -*- coding: utf-8 -*-
"""Prépare les « briefs » par commune pour les rédacteurs : faits Wikipédia filtrés, distance depuis Courgenay,
communes voisines (avec lien si elles sont dans la zone), regroupés en lots d'une douzaine de communes.
Sortie : data/briefs/lot_XX.json et data/briefs/index.json."""
import json, re, math, os, unicodedata, html
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r"[^a-zA-Z0-9]+", '-', s).strip('-').lower()
def clean(t):
    t = re.sub(r'\[[^\]]*\]', '', t or '')
    t = re.sub(r'Cet article concerne[^.]*\.\s*', '', t)
    t = re.sub(r'Pour (les articles|l\'article)[^.]*\.\s*', '', t)
    t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
    return t
def coords(s):
    m = re.findall(r"(\d+)°\s*(\d+)′\s*(\d+)″\s*(nord|sud|est|ouest)", s or '')
    if len(m) < 2: return None
    out = []
    for d, mi, se, h in m[:2]:
        v = int(d) + int(mi) / 60 + int(se) / 3600
        if h in ('sud', 'ouest'): v = -v
        out.append(v)
    return out
def dist(a, b):
    R = 6371; la1, lo1, la2, lo2 = map(math.radians, a + b)
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))
COURGENAY = [47.4044, 7.1272]
CANTON_SHORT = {'JU': 'Jura', 'NE': 'Neuchâtel', 'BE': 'Berne', 'FR': 'Fribourg', 'VD': 'Vaud'}

zone = json.load(open('data/communes_zone.json', encoding='utf-8'))
faits = json.load(open('data/communes_faits.json', encoding='utf-8'))
_dups = {n for n in [x['nom'] for x in zone] if [x['nom'] for x in zone].count(n) > 1}
for c in zone:
    c['slug'] = 'arboriste-' + slugify(c['nom']) + ('-' + c['canton'].lower() if c['nom'] in _dups else '')
    if c['nom'] in _dups: c['nom'] = f"{c['nom']} ({c['canton']})"
    d = (c.get('district') or '').strip('() ')
    if c['canton'] == 'JU' and c['nom'] == 'Moutier': d = 'Delémont'
    c['district'] = d or ('Bienne' if c['canton'] == 'BE' else CANTON_SHORT[c['canton']])
by_name = {c['nom']: c for c in zone}
by_name.update({c['nom'].split(' (')[0]: c for c in zone if ' (' in c['nom']})
KEEP = ['Communes limitrophes', 'NPA', 'Altitude', 'Superficie', 'Densité', 'Gentilé', 'Langue', 'Langues', 'Populationpermanente', 'Localité(s)', 'Site web']
briefs = []
for c in zone:
    f = faits.get(c['page']) or faits.get(c['nom']) or {}
    ib = f.get('infobox') or {}
    co = coords(ib.get('Coordonnées', ''))
    km = round(dist(COURGENAY, co) / 5) * 5 if co else None
    vois_raw = [v.strip(' .') for v in re.split(r',|;', ib.get('Communes limitrophes', '')) if v.strip(' .')]
    vois = []
    for v in vois_raw:
        v2 = re.sub(r'\s*\([^)]*\)', '', v).strip()
        hit = by_name.get(v) or by_name.get(v2)
        vois.append({'nom': v2, 'slug': hit['slug'] if hit else None})
    secs = {}
    for t, body in (f.get('sections') or {}).items():
        if isinstance(body, dict):
            p = body.get('p', ''); p = ' '.join(p) if isinstance(p, list) else str(p)
            li = body.get('li', []); li = li if isinstance(li, list) else [str(li)]
            txt = clean(p) + ((' ' + clean(' ; '.join(li))) if li else '')
        else:
            txt = clean(str(body))
        if txt: secs[t] = txt[:1400]
    briefs.append({
        'slug': c['slug'], 'nom': c['nom'], 'canton': c['canton'], 'canton_nom': CANTON_SHORT[c['canton']], 'district': c['district'],
        'population': c.get('population'), 'tier': c.get('tier'), 'npa': ib.get('NPA'), 'altitude': ib.get('Altitude'), 'superficie': ib.get('Superficie'),
        'densite': ib.get('Densité'), 'gentile': ib.get('Gentilé'), 'langue': ib.get('Langue') or ib.get('Langues'), 'localites': ib.get('Localité(s)'),
        'population_detail': ib.get('Populationpermanente'), 'distance_courgenay_km': km, 'wikipedia': 'https://fr.wikipedia.org/wiki/' + (c['page'] or c['nom']).replace(' ', '_'),
        'intro': clean(f.get('intro', ''))[:1800], 'sections': secs, 'voisins': vois,
    })
# Lots : par canton puis district, ~12 communes
briefs.sort(key=lambda b: (b['canton'], b['district'], -(b['population'] or 0)))
os.makedirs('data/briefs', exist_ok=True)
for fn in os.listdir('data/briefs'): os.remove('data/briefs/' + fn)
lots = []; cur = []
for b in briefs:
    cur.append(b)
    if len(cur) >= 16 and (len(briefs) - sum(len(l) for l in lots) - len(cur)) >= 8: lots.append(cur); cur = []
if cur: lots.append(cur)
index = []
for i, lot in enumerate(lots, 1):
    fn = f'data/briefs/lot_{i:02d}.json'
    json.dump(lot, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    index.append({'lot': fn, 'cantons': sorted({b['canton'] for b in lot}), 'communes': [b['nom'] for b in lot]})
json.dump(index, open('data/briefs/index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(briefs), 'communes,', len(lots), 'lots ;', sum(1 for b in briefs if b['distance_courgenay_km'] is None), 'sans coordonnées')
