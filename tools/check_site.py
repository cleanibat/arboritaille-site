#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle SEO/technique des pages générées : titles et descriptions uniques, un seul H1, liens internes valides,
images avec alt, JSON-LD valide, canonical cohérent, sitemap complet, mots interdits dans le HTML final.
Usage : python3 tools/check_site.py"""
import os, re, glob, json, html, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = 'https://arboritaille.ch/'
BANNED = [r"dans la r[ée]gion", r"entreprise locale", r"\bbas[ée]e?s? [àa] ", r"toute la suisse romande", r"sans nacelle", r"\bengins?\b", r"jura bernois", r"notre [ée]quipe",
          r"\b(le|la|les) meilleur", r"\bn ?°\s?1\b", r"\bleader\b", r"\bincontournable", r"\bexceptionnel", r"\bimbattable", r"\bcertifi", r"\bdipl[ôo]m", r"\bbrevet"]
files = sorted(f for f in glob.glob('*.html') + glob.glob('conseils/*.html') if f != 'maintenance.html')  # page de maintenance (503) hors contrôle SEO
titles, descs, errors, warns = collections.defaultdict(list), collections.defaultdict(list), [], []
existing = set()
for f in files:
    slug = f[:-5]
    existing.add('/' if slug == 'index' else '/' + slug)
existing |= {'/contact.php', '/sitemap.xml', '/robots.txt'}
sitemap = open('sitemap.xml', encoding='utf-8').read() if os.path.exists('sitemap.xml') else ''
sm_urls = set(re.findall(r'<loc>([^<]+)</loc>', sitemap))
for f in files:
    h = open(f, encoding='utf-8').read()
    slug = f[:-5]; url = SITE if slug == 'index' else SITE + slug
    t = re.search(r'<title>(.*?)</title>', h, re.S); t = html.unescape(t.group(1).strip()) if t else ''
    d = re.search(r'<meta name="description" content="([^"]*)"', h); d = html.unescape(d.group(1)) if d else ''
    noindex = 'noindex' in h.split('</head>')[0]
    if not t: errors.append(f'{f}: pas de title')
    elif len(t) > 75 and not noindex: warns.append(f'{f}: title de {len(t)} caractères')
    if not d: errors.append(f'{f}: pas de description')
    elif not noindex and not 90 <= len(d) <= 175: warns.append(f'{f}: description de {len(d)} caractères')
    titles[t].append(f); descs[d].append(f)
    h1 = re.findall(r'<h1[^>]*>', h)
    if len(h1) != 1: errors.append(f'{f}: {len(h1)} balises H1')
    c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    if not c or c.group(1) != url: errors.append(f'{f}: canonical {c.group(1) if c else "absent"} ≠ {url}')
    if not noindex and url not in sm_urls: errors.append(f'{f}: absent du sitemap')
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(ld)
        except Exception as e: errors.append(f'{f}: JSON-LD invalide ({e})')
    for m in re.finditer(r'<img\b[^>]*>', h):
        if 'alt=' not in m.group(0): errors.append(f'{f}: <img> sans alt : {m.group(0)[:80]}')
    for href in set(re.findall(r'href="([^"]+)"', h)):
        if href.startswith(('http', 'tel:', 'mailto:', '#')): continue
        p = href.split('#')[0].split('?')[0]
        if p and p not in existing and not p.startswith(('/img/', '/fonts/', '/style.css', '/main.js')): errors.append(f'{f}: lien interne cassé {href}')
    body = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    body = (t + ' ' + d + ' ' + re.sub(r'<[^>]+>', ' ', body)).lower()
    for rx in BANNED:
        for m in re.finditer(rx, body):
            ctx = body[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')
            errors.append(f'{f}: mot interdit « {m.group(0)} » : …{ctx}…')
for t, fs in titles.items():
    if len(fs) > 1: errors.append(f'title dupliqué « {t[:60]} » : {", ".join(fs)}')
for d, fs in descs.items():
    if len(fs) > 1: errors.append(f'description dupliquée : {", ".join(fs)}')
for u in sm_urls:
    p = u.replace(SITE, '/'); p = '/' if p == '/' else p.rstrip('/')
    if p not in existing: errors.append(f'sitemap : {u} sans fichier')
for w in warns: print('AVERTISSEMENT', w)
for e in errors: print('ERREUR', e)
print(f'\n{len(files)} pages, {len(sm_urls)} URL dans le sitemap : {len(errors)} erreur(s), {len(warns)} avertissement(s)')
sys.exit(1 if errors else 0)
