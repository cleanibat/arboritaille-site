#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validateur des contenus JSON (communes, villes, cantons, guides).
Usage : python3 tools/validate_content.py [chemins…]   (sans argument : tout content/)
Code de sortie 1 s'il y a des erreurs. Les avertissements n'empêchent pas la publication mais doivent être lus."""
import sys, os, re, json, glob, difflib, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BANNED = [
    (r"\bdans la r[ée]gion\b", "« dans la région » interdit"), (r"\bentreprise locale\b", "« entreprise locale » interdit"),
    (r"\bbas[ée]e?s? [àa]\b", "« basé à » interdit (dire « depuis Courgenay »)"), (r"toute la suisse romande", "« toute la Suisse romande » interdit"),
    (r"sans nacelle", "« sans nacelle » interdit"), (r"\bengins?\b", "« engin » interdit (dire « machines »)"), (r"jura bernois", "« Jura bernois » interdit (dire « Berne »)"),
    (r"proche de chez vous", "« proche de chez vous » interdit"), (r"\bnotre [ée]quipe\b|\bnos [ée]quipes\b", "« notre équipe » interdit (entreprise individuelle)"),
    (r"\b(le|la|les) meilleur", "superlatif"), (r"\bn ?°\s?1\b|num[ée]ro (1|un)\b", "superlatif"), (r"\bleader\b", "superlatif"), (r"\bincontournable", "superlatif"),
    (r"\bexceptionnel", "superlatif"), (r"\bimbattable", "superlatif"), (r"\bin[ée]gal[ée]", "superlatif"), (r"\bexcellence\b", "superlatif"), (r"haut de gamme|premium", "superlatif"),
    (r"\bparfait", "superlatif"), (r"100 ?%", "superlatif"), (r"expert reconnu|sp[ée]cialiste reconnu|la r[ée]f[ée]rence\b", "auto-promotion"),
    (r"\bcertifi", "certification non vérifiable"), (r"\bbrevet", "certification non vérifiable"), (r"\bdipl[ôo]m", "certification non vérifiable"), (r"\bmembre de\b", "affiliation non vérifiable"),
    (r"\bASSA\b|\bISA\b|\bSKK\b", "affiliation non vérifiable"), (r"depuis \d+ ans|\d+ ans d'exp[ée]rience|ann[ée]es d'exp[ée]rience", "ancienneté non vérifiable"),
    (r"sous 24 ?h|24 ?h/24|7 ?j/7|dans l'heure", "délai non garanti"), (r"\bgaranti", "garantie non vérifiable"),
    (r"nous avons d[ée]j[àa]|d[ée]j[àa] (intervenu|r[ée]alis[ée]|taill[ée]|abattu|plant[ée])|interven(ons|u) r[ée]guli[èe]rement|nos clients (de|à|d')", "intervention passée inventée"),
    (r"\btu\b|\bton\b|\bta\b|\btes\b", "tutoiement"), (r"!", "point d'exclamation"),
]
REAL_SITES = {'arboriste-porrentruy', 'arboriste-neuchatel', 'arboriste-bienne', 'arboriste-port', 'arboriste-courgenay'}
ICONS = {'TREE', 'LEAF', 'MOUNT', 'HOME', 'WIND', 'WARN', 'SHIELD', 'PIN', 'CLOCK', 'USERS', 'SPROUT', 'DOC', 'SEARCH', 'CABLE', 'STUMP', 'AXE', 'SCISS', 'CRANE', 'ARROW', 'LINK', 'CUT', 'SHRINK', 'LIFT', 'PLUS'}
IMAGES = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob('img/*.jpg')}
STATIC = {'index', 'contact', 'a-propos', 'conseils', 'zone-intervention', 'collectivites-entreprises', 'mentions-legales', 'protection-des-donnees', 'merci', 'plan-du-site',
          'elagage-taille-arbres', 'abattage-demontage', 'urgence-tempete-arbre-dangereux', 'rognage-souche', 'haubanage', 'plantation-arbres', 'diagnostic-expertise-arbre',
          'arboriste-canton-du-jura', 'arboriste-canton-de-neuchatel', 'arboriste-bienne-canton-de-berne', 'arboriste-canton-de-fribourg', 'arboriste-canton-de-vaud'}
TAGS_OK = {'p', 'a', 'strong', 'em', 'br', 'ul', 'ol', 'li', 'span'}

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r"[^a-zA-Z0-9]+", '-', s).strip('-').lower()
def strip_tags(s): return re.sub(r'<[^>]+>', ' ', s or '')
def words(s): return len(strip_tags(s).split())
def norm(s): return re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', strip_tags(s).lower()).encode('ascii', 'ignore').decode())

BRIEFS = {}
for f in glob.glob('data/briefs/lot_*.json'):
    for b in json.load(open(f, encoding='utf-8')): BRIEFS[b['slug']] = b
COMMUNE_SLUGS = set(BRIEFS)
GUIDE_SLUGS = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob('content/guides/*.json')}
VILLE_SLUGS = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob('content/villes/*.json')}
ALL_SLUGS = STATIC | COMMUNE_SLUGS | VILLE_SLUGS | {'conseils/' + g for g in GUIDE_SLUGS}

errors, warnings = [], []
def err(f, m): errors.append(f'{f}: {m}')
def warn(f, m): warnings.append(f'{f}: {m}')

def walk_strings(o, path=''):
    if isinstance(o, str): yield path, o
    elif isinstance(o, dict):
        for k, v in o.items(): yield from walk_strings(v, f'{path}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk_strings(v, f'{path}[{i}]')

def check_text_rules(f, data, is_commune_slug=None):
    for path, s in walk_strings(data):
        if path.endswith('.url') or 'sources' in path or path.endswith('hero_img') or path.endswith('cta_img') or path.endswith('.img') or path.endswith('icone'): continue
        low = s.lower()
        for rx, msg in BANNED:
            if re.search(rx, low):
                if msg == 'intervention passée inventée' and is_commune_slug in REAL_SITES: continue
                if msg == 'point d\'exclamation' and 'q' in path.split('.')[-1]: pass
                err(f, f'{msg} dans {path} : « {s[:90]} »')
        # balises
        for t in re.findall(r'<\s*/?\s*([a-zA-Z0-9]+)', s):
            if t.lower() not in TAGS_OK: err(f, f'balise <{t}> non autorisée dans {path}')
        # liens
        for href in re.findall(r'href="([^"]+)"', s):
            if href.startswith(('tel:', 'mailto:', '#')): continue
            if href.startswith('http'):
                if not re.search(r'\.(ch|admin\.ch)(/|$)', href) and 'fedlex' not in href and 'lexfind' not in href: warn(f, f'lien externe non officiel dans {path} : {href}')
                continue
            slug = href.lstrip('/').split('#')[0].split('?')[0]
            if slug == '': continue
            if slug not in ALL_SLUGS: err(f, f'lien interne vers une page inexistante dans {path} : {href}')
        # paragraphes
        if path.split('.')[-1] in ('intro', 'reglement', 'a', 'texte', 'lead', 'p', 'notice') or re.search(r'\.p\[\d+\]$', path):
            lim_err, lim_warn = (95, 80) if path.endswith('reglement') else (60, 45)
            for para in re.split(r'</p>|<br\s*/?>', s):
                w = words(para)
                if w > lim_err: err(f, f'paragraphe de {w} mots (> {lim_err}) dans {path}')
                elif w > lim_warn: warn(f, f'paragraphe de {w} mots (> {lim_warn}) dans {path}')

def check_commune(f, X, slug):
    b = BRIEFS.get(slug)
    if not b: err(f, 'slug inconnu dans les briefs'); return
    nom = b['nom']; nomn = norm(nom)
    req = ['title', 'desc', 'eyebrow', 'h1', 'lead', 'points', 'intro_h2', 'intro', 'faits', 'reglement', 'contexte', 'faq']
    for k in req:
        if k not in X: err(f, f'clé manquante : {k}')
    if errors and any(f in e for e in errors[-len(req):]): return
    for k in ('title', 'h1', 'desc', 'lead', 'intro'):
        if nomn not in norm(X.get(k, '')): err(f, f'le nom de la commune manque dans {k}')
    t = X['title']
    if not t.endswith('| Arboritaille'): warn(f, 'title sans « | Arboritaille » final')
    if len(t) > 75: warn(f, f'title long ({len(t)} car.)')
    if not 100 <= len(X['desc']) <= 170: warn(f, f'desc de {len(X["desc"])} caractères (viser 120-160)')
    if words(X['lead']) > 45: err(f, f'lead de {words(X["lead"])} mots')
    if len(X['points']) != 4: err(f, '4 puces attendues')
    if not 2 <= X['intro'].count('<p>') <= 4: err(f, f'intro : {X["intro"].count("<p>")} paragraphes (2 à 4 attendus)')
    if len(X['faits']) != 4 or any(len(x) != 2 for x in X['faits']): err(f, 'faits : 4 paires [label, valeur] attendues')
    else:
        joined = ' '.join(v for _, v in X['faits'])
        nums = [re.sub(r'[\s  ]', '', n) for n in re.findall(r'\d[\d\s  ]*', joined)]
        ok_nums = set()
        for v in [b.get('population'), b.get('altitude'), b.get('superficie'), b.get('npa'), b.get('distance_courgenay_km'), b.get('densite'), b.get('population_detail')]:
            if v is None: continue
            for n in re.findall(r'\d[\d\s  ,.]*', str(v)): ok_nums.add(re.sub(r'[\s  ]', '', n).rstrip('.,'))
        for n in nums:
            if n in ('2025', '2024', '2023', '1', '2', '3', '4', '5'): continue
            if not any(n == o or n in o or o in n for o in ok_nums): err(f, f'fait chiffré « {n} » absent du brief (population {b.get("population")}, altitude {b.get("altitude")}, superficie {b.get("superficie")}, distance {b.get("distance_courgenay_km")})')
    if not 3 <= len(X['contexte']) <= 4: err(f, 'contexte : 3 ou 4 blocs attendus')
    for c in X['contexte']:
        if c.get('icone') not in ICONS: err(f, f'icône inconnue : {c.get("icone")}')
        if words(c.get('texte', '')) > 50: err(f, f'contexte « {c.get("titre")} » trop long')
    if not 4 <= len(X['faq']) <= 6: err(f, f'faq : {len(X["faq"])} questions (4 à 5 attendues)')
    if sum(1 for q in X['faq'] if nomn in norm(q['q'] + ' ' + q['a'])) < 2: err(f, 'au moins 2 questions de FAQ doivent citer la commune')
    for q in X['faq']:
        w = words(q['a'])
        if w < 15 or w > 75: warn(f, f'réponse FAQ de {w} mots : « {q["q"][:50]} »')
    for k in ('hero_img', 'cta_img'):
        if X.get(k) and X[k] not in IMAGES: err(f, f'{k} inconnu : {X[k]}')
    if X.get('galerie') and slug not in REAL_SITES: err(f, 'galerie réservée aux communes avec photos réelles')
    if 'v[ée]rifi' not in X['reglement'] and not re.search(r'v[ée]rifi', X['reglement'], re.I): warn(f, 'reglement sans phrase « nous vérifions… »')
    # régle communale inventée ?
    for m in re.findall(r'(\d+)\s?cm', strip_tags(X['reglement'])):
        allowed = {'JU': {'20'}, 'NE': {'60'}, 'BE': set(), 'FR': set(), 'VD': {'40', '20', '30'}}[b['canton']]
        if m not in allowed: err(f, f'seuil « {m} cm » dans reglement non prévu pour le canton {b["canton"]}')
    if b['canton'] == 'JU' and '20' in strip_tags(X['reglement']) and 'Delémont' not in X['reglement'] and nom != 'Delémont': warn(f, 'seuil 20 cm cité hors Delémont : vérifier la formulation (exemple, pas règle locale)')
    if b['canton'] == 'NE' and '60' in strip_tags(X['reglement']) and nom not in ('Neuchâtel', 'Peseux', 'Corcelles-Cormondrèche', 'Valangin') and 'Neuchâtel' not in X['reglement']: warn(f, 'seuil 60 cm cité : doit être attribué à la commune de Neuchâtel')
    check_text_rules(f, X, slug)

def check_ville(f, X, slug):
    for k in ['service', 'commune', 'h1_plain', 'title', 'desc', 'eyebrow', 'h1', 'lead', 'points', 'intro_h2', 'intro', 'contexte', 'faq']:
        if k not in X: err(f, f'clé manquante : {k}')
    if X.get('service') not in ('elagage-taille-arbres', 'abattage-demontage'): err(f, f'service inconnu : {X.get("service")}')
    if X.get('commune') not in BRIEFS: err(f, f'commune inconnue : {X.get("commune")}')
    else:
        nomn = norm(BRIEFS[X['commune']]['nom'])
        for k in ('title', 'h1', 'desc', 'lead', 'intro', 'h1_plain'):
            if nomn not in norm(X.get(k, '')): err(f, f'le nom de la ville manque dans {k}')
        exp = ('elagage-' if X.get('service') == 'elagage-taille-arbres' else 'abattage-arbre-') + X['commune'].replace('arboriste-', '')
        if slug != exp: err(f, f'nom de fichier attendu : {exp}.json')
    if X.get('points') and len(X['points']) != 4: err(f, '4 puces attendues')
    if X.get('faq') and not 4 <= len(X['faq']) <= 6: err(f, 'faq : 4 à 5 questions attendues')
    for c in X.get('contexte', []):
        if c.get('icone') not in ICONS: err(f, f'icône inconnue : {c.get("icone")}')
    check_text_rules(f, X)

def check_canton(f, K, code):
    for k in ['title', 'desc', 'h1', 'lead', 'points', 'resume', 'intro_h2', 'intro', 'contexte', 'reglement', 'faq']:
        if k not in K: err(f, f'{code} : clé manquante : {k}')
    if K.get('faq') and len(K['faq']) < 4: err(f, f'{code} : faq trop courte')
    for c in K.get('contexte', []):
        if c.get('icone') not in ICONS: err(f, f'{code} : icône inconnue : {c.get("icone")}')
    check_text_rules(f + ':' + code, K)

def check_guide(f, G):
    for k in ['title', 'desc', 'titre_court', 'h1', 'lead', 'date', 'sections']:
        if k not in G: err(f, f'clé manquante : {k}')
    if len(G.get('titre_court', '')) > 50: warn(f, 'titre_court > 50 caractères')
    total = sum(words(' '.join(s.get('p', []))) + words(' '.join(s.get('ul', []) + s.get('ol', []))) for s in G.get('sections', []))
    if total < 700: warn(f, f'guide court ({total} mots)')
    if total > 2200: warn(f, f'guide long ({total} mots)')
    if not G.get('sources'): warn(f, 'aucune source')
    if G.get('img') and G['img'] not in IMAGES: err(f, f'img inconnue : {G["img"]}')
    if not re.match(r'\d{4}-\d{2}-\d{2}$', str(G.get('date', ''))): err(f, 'date au format AAAA-MM-JJ attendue')
    check_text_rules(f, {k: v for k, v in G.items() if k != 'sources'})

def similarity_check(files):
    intros = {}
    for f in files:
        try: X = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        slug = os.path.splitext(os.path.basename(f))[0]
        b = BRIEFS.get(slug)
        txt = norm((X.get('intro', '') + ' ' + ' '.join(c.get('texte', '') for c in X.get('contexte', []))))
        if b: txt = txt.replace(norm(b['nom']), 'X')
        intros[f] = txt
    keys = list(intros)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b2 = intros[keys[i]], intros[keys[j]]
            if not a or not b2: continue
            r = difflib.SequenceMatcher(None, a, b2).quick_ratio()
            if r > 0.55:
                r2 = difflib.SequenceMatcher(None, a, b2).ratio()
                if r2 > 0.55: err(keys[i], f'intro trop semblable à {os.path.basename(keys[j])} (similarité {r2:.2f})')

def main(paths):
    files = []
    for p in paths:
        if os.path.isdir(p): files += sorted(glob.glob(os.path.join(p, '**', '*.json'), recursive=True))
        else: files.append(p)
    communes = []
    for f in files:
        rel = os.path.relpath(f)
        try: data = json.load(open(f, encoding='utf-8'))
        except Exception as e: err(rel, f'JSON invalide : {e}'); continue
        slug = os.path.splitext(os.path.basename(f))[0]
        if '/communes/' in f.replace('\\', '/'): check_commune(rel, data, slug); communes.append(f)
        elif '/villes/' in f.replace('\\', '/'): check_ville(rel, data, slug)
        elif '/guides/' in f.replace('\\', '/'): check_guide(rel, data)
        elif slug == 'cantons':
            for code, K in data.items(): check_canton(rel, K, code)
    if len(communes) > 1 or (communes and '--all-similar' in sys.argv):
        allc = sorted(glob.glob('content/communes/*.json')) if '--all-similar' in sys.argv else communes
        similarity_check(allc)
    for w in warnings: print('AVERTISSEMENT', w)
    for e in errors: print('ERREUR', e)
    print(f'\n{len(files)} fichier(s) : {len(errors)} erreur(s), {len(warnings)} avertissement(s)')
    sys.exit(1 if errors else 0)

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    main(args or ['content'])
