#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copie du site dans docs/ pour l'aperçu GitHub Pages (https://cleanibat.github.io/arboritaille-site/) :
chemins absolus préfixés, noindex, formulaire désactivé (aperçu illustratif). La production (IONOS) sert la racine."""
import os, re, shutil, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PREFIX = '/arboritaille-site'
OUT = 'docs'
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
for d in ('img', 'fonts'): shutil.copytree(d, os.path.join(OUT, d))
for f in ('style.css', 'main.js', 'robots.txt'): shutil.copy(f, OUT)
open(os.path.join(OUT, '.nojekyll'), 'w').close()
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
css = open(os.path.join(OUT, 'style.css'), encoding='utf-8').read().replace('url(/', f'url({PREFIX}/').replace("url('/", f"url('{PREFIX}/").replace('url("/', f'url("{PREFIX}/')
open(os.path.join(OUT, 'style.css'), 'w', encoding='utf-8').write(css)
fc = open(os.path.join(OUT, 'fonts', 'fonts.css'), encoding='utf-8').read().replace('url(/', f'url({PREFIX}/')
open(os.path.join(OUT, 'fonts', 'fonts.css'), 'w', encoding='utf-8').write(fc)
n = 0
for f in glob.glob('*.html') + glob.glob('conseils/*.html'):
    h = open(f, encoding='utf-8').read()
    h = re.sub(r'(href|src|action|srcset)="/(?!/)', lambda m: f'{m.group(1)}="{PREFIX}/', h)
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex, nofollow">')
    h = h.replace(f'action="{PREFIX}/contact.php"', 'action="#" onsubmit="alert(\'Aperçu : le formulaire est actif uniquement sur arboritaille.ch\');return false"')
    # liens « racine » du type href="/arboritaille-site/" déjà traités ; ancre accueil
    dest = os.path.join(OUT, f)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(h); n += 1
print(f'aperçu : {n} pages dans {OUT}/')
