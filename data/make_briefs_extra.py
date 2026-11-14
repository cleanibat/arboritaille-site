# -*- coding: utf-8 -*-
"""Briefs des pages villes et cantons, dérivés des lots de communes et de reglements_cantons.json.
Sortie : data/briefs/villes.json et data/briefs/cantons.json (à relancer après make_briefs.py)."""
import json, glob, os, collections
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
allb = [b for f in sorted(glob.glob('data/briefs/lot_*.json')) for b in json.load(open(f, encoding='utf-8'))]
reg = json.load(open('data/reglements_cantons.json', encoding='utf-8'))
VILLES = ['Delémont', 'Porrentruy', 'Moutier', 'Neuchâtel', 'La Chaux-de-Fonds', 'Le Locle', 'Bienne', 'Fribourg', 'Bulle',
          'Yverdon-les-Bains', 'Lausanne', 'Vevey', 'Montreux', 'Payerne']
by = {b['nom']: b for b in allb}
out = []
for v in VILLES:
    b = dict(by[v]); b['commune'] = b['slug']; b['slug_ville'] = b['slug'].replace('arboriste-', '')
    b['pages'] = ['elagage-' + b['slug_ville'], 'abattage-arbre-' + b['slug_ville']]
    out.append(b)
json.dump(out, open('data/briefs/villes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cant = {}
for code in ['JU', 'NE', 'BE', 'FR', 'VD']:
    cs = [b for b in allb if b['canton'] == code]
    d = collections.defaultdict(list)
    for b in cs: d[b['district']].append(b['nom'])
    big = sorted(cs, key=lambda b: -(b['population'] or 0))[:12]
    cant[code] = {'nom': cs[0]['canton_nom'], 'nb_communes': len(cs), 'districts': d,
                  'grandes_communes': [{'nom': b['nom'], 'slug': b['slug'], 'population': b['population'], 'altitude': b['altitude'], 'distance_courgenay_km': b['distance_courgenay_km']} for b in big],
                  'distance_min_km': min(b['distance_courgenay_km'] for b in cs if b['distance_courgenay_km'] is not None),
                  'distance_max_km': max(b['distance_courgenay_km'] for b in cs if b['distance_courgenay_km'] is not None),
                  'reglement': reg.get(code)}
json.dump(cant, open('data/briefs/cantons.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'villes ;', {k: v['nb_communes'] for k, v in cant.items()})
