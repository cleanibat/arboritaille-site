# -*- coding: utf-8 -*-
"""Génère le site arboritaille.ch (statique, SEO).

Entrées :
  content_static.py        textes des pages fixes (accueil, services, à propos, contact, légal)
  content/cantons.json     textes des pages cantons (hub de zone)
  content/communes/*.json  une fiche par commune (écrite par les rédacteurs, validée)
  content/villes/*.json    pages service × grande ville (elagage-<ville>, abattage-arbre-<ville>)
  content/guides/*.json    articles conseils
  data/communes_zone.json  liste des communes (Wikipédia / OFS)
Sortie : fichiers .html à la racine (URL propres via .htaccess), conseils/, sitemap.xml, robots.txt.
"""
import os, re, json, glob, html, datetime, unicodedata
import content_static as C

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SITE = 'https://arboritaille.ch/'
BRAND = 'Arboritaille'
PHONE_INTL = '+41783065304'; PHONE = '078 306 53 04'; EMAIL = 'contact@arboritaille.ch'
ADDRESS = dict(street='Derrière-Metthiez 13', zip='2950', city='Courgenay', canton='JU', country='CH')
GTM_ID = 'GTM-WMF2BV3S'
TODAY = datetime.date.today().isoformat()
BUILD_VER = datetime.datetime.now().strftime('%Y%m%d%H%M')

# ---------------- Icônes ----------------
def _i(d): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I = dict(
PHONE=_i('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>'),
ARROW=_i('<path d="M5 12h14M13 6l6 6-6 6"/>'), CHECK=_i('<path d="M20 6 9 17l-5-5"/>'), CK3=_i('<path d="M20 6 9 17l-5-5"/>'),
PIN=_i('<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
LOCK=_i('<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'),
MAIL=_i('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/>'),
SHIELD=_i('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>'),
SHIELD0=_i('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
LEAF=_i('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'),
DOC=_i('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>'),
WARN=_i('<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>'),
TREE=_i('<path d="M12 22v-6"/><path d="M8 16h8l-2-4h1l-3-5h.5L12 3l-.5 4H12l-3 5h1l-2 4z"/>'),
SCISS=_i('<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/>'),
AXE=_i('<path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M15 13 9 7l4-4 6 6h3a8 8 0 0 1-7 7z"/>'),
SEARCH=_i('<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>'),
SPROUT=_i('<path d="M7 20h10M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>'),
LINK=_i('<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>'),
STUMP=_i('<ellipse cx="12" cy="7" rx="8" ry="3"/><path d="M4 7v10c0 1.7 3.6 3 8 3s8-1.3 8-3V7"/><ellipse cx="12" cy="7" rx="3" ry="1.2"/>'),
CRANE=_i('<path d="M3 21h18M6 21V8l12-5v18M6 8h12M14 8v6M14 14h3"/>'),
CUT=_i('<path d="M6 3 3 6l3 3M18 3l3 3-3 3M3 6h18M12 6v15"/>'), SHRINK=_i('<path d="M21 3 3 21M21 3h-6M21 3v6M3 21h6M3 21v-6"/>'),
LIFT=_i('<path d="M12 22V8M5 12l7-7 7 7M4 22h16"/>'), PLUS=_i('<path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/>'),
CABLE=_i('<path d="M12 3v18M6 9c0 3.3 2.7 6 6 6s6-2.7 6-6"/><path d="M4 6c0 4.4 3.6 8 8 8s8-3.6 8-8"/>'),
WIND=_i('<path d="M9.6 4.6A2 2 0 1 1 11 8H2M12.6 19.4A2 2 0 1 0 14 16H2M17.7 7.7A2.5 2.5 0 1 1 19.5 12H2"/>'),
MOUNT=_i('<path d="m8 3 4 8 5-5 5 15H2L8 3z"/>'), HOME=_i('<path d="m3 11 9-8 9 8v9a2 2 0 0 1-2 2h-4v-6h-6v6H5a2 2 0 0 1-2-2z"/>'),
BURGER=_i('<path d="M3 6h18M3 12h18M3 18h18"/>'), CLOCK=_i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
USERS=_i('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
)

# ---------------- Utilitaires ----------------
def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r"[^a-zA-Z0-9]+", '-', s).strip('-').lower()
    return s
def esc(s): return html.escape(str(s), quote=True)
def url(slug): return SITE + slug[5:] if slug.startswith('index#') else (SITE if slug in ('index', '') else SITE + slug)
def href(slug): return '/' + slug[5:] if slug.startswith('index#') else ('/' if slug in ('index', '') else '/' + slug)
PAGES = []  # (slug, lastmod, priority)
def register(slug, priority='0.6', lastmod=None): PAGES.append((slug, lastmod or TODAY, priority))

def picture(name, alt, cls='', lazy=True, sizes='(max-width: 700px) 100vw, 50vw', w=None, h=None, card=False, style=''):
    """<picture> WebP + JPEG. name sans extension (img/<name>.jpg)."""
    src = f'img/w/{name}-800.webp' if card else f'img/w/{name}.webp'
    attrs = f' class="{cls}"' if cls else ''
    attrs += ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    if w and h: attrs += f' width="{w}" height="{h}"'
    if style: attrs += f' style="{style}"'
    return (f'<picture><source type="image/webp" srcset="/{src}">'
            f'<img src="/img/{name}.jpg" alt="{esc(alt)}"{attrs}></picture>')
IMG_SIZE = {}
try:
    from PIL import Image
    for f in glob.glob('img/*.jpg'):
        with Image.open(f) as im: IMG_SIZE[os.path.splitext(os.path.basename(f))[0]] = im.size
except Exception:
    pass
def pic(name, alt, cls='', lazy=True, card=False, style=''):
    w, h = IMG_SIZE.get(name, (None, None))
    return picture(name, alt, cls, lazy, w=w, h=h, card=card, style=style)

# ---------------- Données ----------------
COMMUNES = json.load(open('data/communes_zone.json', encoding='utf-8'))
CANTON_SLUG = {'JU': 'arboriste-canton-du-jura', 'NE': 'arboriste-canton-de-neuchatel', 'BE': 'arboriste-bienne-canton-de-berne', 'FR': 'arboriste-canton-de-fribourg', 'VD': 'arboriste-canton-de-vaud'}
CANTON_NAME = {'JU': 'Canton du Jura', 'NE': 'Canton de Neuchâtel', 'BE': 'Bienne et canton de Berne', 'FR': 'Canton de Fribourg', 'VD': 'Canton de Vaud'}
CANTON_SHORT = {'JU': 'Jura', 'NE': 'Neuchâtel', 'BE': 'Berne', 'FR': 'Fribourg', 'VD': 'Vaud'}
_dups = {n for n in [x['nom'] for x in COMMUNES] if [x['nom'] for x in COMMUNES].count(n) > 1}
for c in COMMUNES:
    c['slug'] = 'arboriste-' + slugify(c['nom']) + ('-' + c['canton'].lower() if c['nom'] in _dups else '')
    c['nom_court'] = c['nom']
    if c['nom'] in _dups: c['nom'] = f"{c['nom']} ({c['canton']})"
    d = (c.get('district') or '').strip('() ')
    if c['canton'] == 'JU' and c['nom'] == 'Moutier': d = 'Delémont'
    c['district'] = d or ('Bienne' if c['canton'] == 'BE' else CANTON_SHORT[c['canton']])
BY_SLUG = {c['slug']: c for c in COMMUNES}
def load_json_dir(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, '*.json'))):
        out[os.path.splitext(os.path.basename(f))[0]] = json.load(open(f, encoding='utf-8'))
    return out
COMMUNE_CONTENT = load_json_dir('content/communes')
VILLE_CONTENT = load_json_dir('content/villes')
GUIDES = load_json_dir('content/guides')
CANTONS = json.load(open('content/cantons.json', encoding='utf-8')) if os.path.exists('content/cantons.json') else {}

SERVICES = C.SERVICES  # liste ordonnée de dicts (slug, nav, title, ...)
SERVICE_BY_SLUG = {s['slug']: s for s in SERVICES}

# ---------------- Gabarit ----------------
GTM_HEAD = (f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}'
            f'gtag("consent","default",{{ad_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",analytics_storage:"denied",wait_for_update:500}});</script>\n'
            f'<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{\'gtm.start\':new Date().getTime(),event:\'gtm.js\'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!=\'dataLayer\'?\'&l=\'+l:\'\';j.async=true;j.src=\'https://www.googletagmanager.com/gtm.js?id=\'+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,\'script\',\'dataLayer\',\'{GTM_ID}\');</script>\n<!-- End Google Tag Manager -->') if GTM_ID else ''
GTM_BODY = (f'<!-- Google Tag Manager (noscript) -->\n<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n<!-- End Google Tag Manager (noscript) -->') if GTM_ID else ''

BUSINESS_ID = SITE + '#entreprise'
def business_jsonld():
    return {
        '@type': ['LocalBusiness', 'ProfessionalService'], '@id': BUSINESS_ID, 'name': BRAND,
        'alternateName': 'Arboritaille – Robin Humbert, arboriste-grimpeur',
        'description': 'Arboriste-grimpeur : taille et entretien des arbres, élagage, abattage et démontage, rognage de souche, plantation, haubanage et diagnostic, pour les particuliers, entreprises et collectivités du Jura, de Neuchâtel, de Bienne, de Fribourg et du canton de Vaud.',
        'url': SITE, 'telephone': PHONE_INTL, 'email': EMAIL, 'image': SITE + 'img/arboriste_grimpeur-19.jpg', 'logo': SITE + 'img/logo-entreprise-icon-sans-fond.svg',
        'founder': {'@type': 'Person', 'name': 'Robin Humbert', 'jobTitle': 'Arboriste-grimpeur'},
        'address': {'@type': 'PostalAddress', 'streetAddress': ADDRESS['street'], 'postalCode': ADDRESS['zip'], 'addressLocality': ADDRESS['city'], 'addressRegion': ADDRESS['canton'], 'addressCountry': ADDRESS['country']},
        'geo': {'@type': 'GeoCoordinates', 'latitude': 47.4044, 'longitude': 7.1272},
        'areaServed': [{'@type': 'AdministrativeArea', 'name': n} for n in ['Canton du Jura', 'Canton de Neuchâtel', 'Jura bernois', 'Bienne', 'Canton de Fribourg', 'Canton de Vaud']],
        'knowsLanguage': ['fr', 'de'], 'currenciesAccepted': 'CHF', 'priceRange': 'Devis gratuit',
        'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '08:00', 'closes': '18:00'}],
        'hasMap': C.GBP_URL,
        'sameAs': C.SAME_AS,
    }
def jsonld(*objs):
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [o for o in objs if o]}, ensure_ascii=False) + '</script>'
def breadcrumb_ld(trail):
    return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': url(s)} for i, (n, s) in enumerate(trail)]}
def faq_ld(items):
    # FAQPage : résultats enrichis supprimés par Google (mai 2026), documentation retirée. La FAQ reste visible, sans balisage.
    return None

def head(slug, title, desc, og_img='arboriste_grimpeur-19', ld=None, noindex=False, preload=None):
    canon = url(slug)
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large'
    pre = f'<link rel="preload" as="image" href="/img/w/{preload}.webp" type="image/webp">' if preload else ''
    return f'''<!DOCTYPE html>
<html lang="fr-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_CH"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}img/{og_img}.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#163223">
<link rel="icon" href="/img/logo-entreprise-icon-sans-fond.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/fraunces-600-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter-400-latin.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/fonts/fonts.css?v={BUILD_VER}">
<link rel="stylesheet" href="/style.css?v={BUILD_VER}">
{ld or ''}
{GTM_HEAD}
</head>
<body>
{GTM_BODY}
'''

def header(current=''):
    subs = ''.join(f'<li><a href="{href(s["slug"])}">{esc(s["nav"])}<small>{esc(s["nav_sub"])}</small></a></li>' for s in SERVICES)
    def cur(s): return ' aria-current="page"' if s == current else ''
    return f'''<a class="sr-only" href="#contenu">Aller au contenu</a>
<header class="header">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Arboritaille, accueil"><img src="/img/logo-site-arboritaille-sans-ombre.svg" alt="Arboritaille" width="200" height="38"></a>
    <nav aria-label="Navigation principale">
      <ul class="nav">
        <li><button type="button" aria-haspopup="true">Services</button><ul class="sub">{subs}</ul></li>
        <li><a href="/zone-intervention"{cur('zone-intervention')}>Zone d'intervention</a></li>
        <li><a href="/conseils"{cur('conseils')}>Conseils</a></li>
        <li><a href="/a-propos"{cur('a-propos')}>À propos</a></li>
        <li><a href="/contact"{cur('contact')}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{PHONE_INTL}">{I['PHONE']}<span><small>Appelez-nous</small>{PHONE}</span></a>
      <a class="btn btn-primary" href="/contact">Devis gratuit</a>
      <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false">{I['BURGER']}</button>
    </div>
  </div>
</header>
<main id="contenu">
'''

def footer():
    serv = ''.join(f'<li><a href="{href(s["slug"])}">{esc(s["nav"])}</a></li>' for s in SERVICES)
    zones = ''.join(f'<li><a href="{href(CANTON_SLUG[c])}">{esc(CANTON_NAME[c])}</a></li>' for c in ['JU', 'NE', 'BE', 'FR', 'VD'])
    guides = ''.join(f'<li><a href="/conseils/{g}">{esc(GUIDES[g]["titre_court"])}</a></li>' for g in list(GUIDES)[:6])
    return f'''
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><img src="/img/logo-entreprise-icon-sans-fond.svg" alt="" width="40" height="40"><div><strong>Arboritaille</strong>Arboriste-grimpeur · Robin Humbert</div></div>
        <address>{ADDRESS['street']}, {ADDRESS['zip']} {ADDRESS['city']} (JU)<br><a href="tel:{PHONE_INTL}">+41 78 306 53 04</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address>
        <p style="margin-top:.8rem">Devis et visite gratuits, réponse sous 48 h ouvrées. Nous répondons aussi en allemand par écrit.</p>
      </div>
      <div><h4>Services</h4><ul>{serv}<li><a href="/collectivites-entreprises">Collectivités et entreprises</a></li></ul></div>
      <div><h4>Zone d'intervention</h4><ul><li><a href="/zone-intervention">Toutes les communes</a></li>{zones}</ul></div>
      <div><h4>Conseils</h4><ul><li><a href="/conseils">Tous les conseils</a></li>{guides}</ul></div>
    </div>
    <div class="footer-bottom">
      <span>© {datetime.date.today().year} Arboritaille – Robin Humbert, Courgenay. Tous droits réservés.</span>
      <span><a href="/a-propos">À propos</a> · <a href="/contact">Contact</a> · <a href="/mentions-legales">Mentions légales</a> · <a href="/protection-des-donnees">Protection des données</a> · <a href="#" data-consent-open>Cookies</a> · <a href="/plan-du-site">Plan du site</a></span>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="btn btn-outline" href="tel:{PHONE_INTL}">{I['PHONE']} Appeler</a>
  <a class="btn btn-primary" href="/contact">Devis gratuit</a>
</div>
<div class="consent" id="consent" role="dialog" aria-label="Cookies">
  <p><strong>Cookies.</strong> Ce site utilise des cookies de mesure et de publicité (Google) uniquement si vous l'acceptez. Votre choix est conservé six mois. <a href="/protection-des-donnees">En savoir plus</a></p>
  <div class="consent-actions"><button class="btn btn-outline" type="button" data-consent="no">Tout refuser</button><button class="btn btn-primary" type="button" data-consent="yes">Tout accepter</button></div>
</div>
<script src="/main.js?v={BUILD_VER}" defer></script>
</body>
</html>
'''

def write(slug, html_body, subdir=''):
    path = (subdir + '/' if subdir else '') + (slug if slug != 'index' else 'index') + '.html'
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html_body)

# ---------------- Composants ----------------
def crumbs(trail):
    lis = ''.join((f'<li><a href="{href(s)}">{esc(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(n)}</li>') for i, (n, s) in enumerate(trail))
    return f'<ol class="crumbs">{lis}</ol>'

def form(page_name, title='Recevez votre devis gratuit', sub='Décrivez-nous votre arbre en quelques mots. Nous vous rappelons pour fixer une visite.', options=None, city_ph='Delémont, Neuchâtel, Bienne…'):
    options = options or C.FORM_OPTIONS
    opts = ''.join('<option>' + esc(o) + '</option>' for o in options)
    return f'''<div class="form-card" id="devis">
      <h2>{esc(title)}</h2>
      <p class="sub">{esc(sub)}</p>
      <form action="/contact.php" method="POST" id="devisForm">
        <input type="hidden" name="Sujet" value="Nouvelle demande de devis – arboritaille.ch">
        <input type="hidden" name="lp" value="{esc(page_name)}">
        <input type="hidden" name="Source" value="Site arboritaille.ch – {esc(page_name)}">
        <input type="hidden" name="Origine" value="Site">
        <input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
        <div class="field-row">
          <div class="field"><label for="nom">Nom et prénom</label><input id="nom" name="Nom" type="text" required autocomplete="name" placeholder="Jean Dupont"></div>
          <div class="field"><label for="tel">Téléphone</label><input id="tel" name="Téléphone" type="tel" required autocomplete="tel" placeholder="078 000 00 00"></div>
        </div>
        <div class="field-row">
          <div class="field"><label for="email">E-mail</label><input id="email" name="Email" type="email" required autocomplete="email" placeholder="nom@exemple.ch"></div>
          <div class="field"><label for="localite">Localité</label><input id="localite" name="Localité" type="text" required autocomplete="address-level2" placeholder="{esc(city_ph)}"></div>
        </div>
        <div class="field"><label for="besoin">Votre besoin</label>
          <select id="besoin" name="Besoin" required><option value="" disabled selected>Choisir…</option>{opts}</select>
        </div>
        <div class="field"><label for="msg">Décrivez votre situation (facultatif)</label><textarea id="msg" name="Message" placeholder="Essence, hauteur approximative, accès, ce qui vous inquiète…"></textarea></div>
        <button class="btn btn-primary btn-block" type="submit">Envoyer ma demande</button>
        <p class="form-note">{I['MAIL']} Vous pouvez aussi nous écrire en allemand : nous répondons par écrit en allemand, par téléphone en français.</p>
        <p class="form-note">{I['LOCK']} Vos données servent uniquement à traiter votre demande. Aucune revente, aucun démarchage. <a href="/protection-des-donnees">Protection des données</a></p>
      </form>
    </div>'''

def hero(img, pos, eyebrow, h1, lead, points, formhtml=None, trail=None, solo=False):
    pts = ''.join(f'<li>{I["CHECK"]}{p}</li>' for p in points)
    w, h = IMG_SIZE.get(img, (None, None))
    bg = f'<picture><source type="image/webp" srcset="/img/w/{img}.webp"><img class="hero-bg" src="/img/{img}.jpg" alt="" fetchpriority="high" decoding="async" style="object-position:{pos}"{f" width={w} height={h}" if w else ""}></picture>'
    cr = crumbs(trail) if trail else ''
    return f'''<section class="hero{' hero-solo' if solo else ''}">
  {bg}
  <div class="wrap">
    <div>
      {cr}<span class="eyebrow" style="color:var(--yellow)">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{'#devis' if formhtml else '/contact'}">Demander un devis gratuit {I['ARROW']}</a>
        <a class="btn btn-ghost" href="tel:{PHONE_INTL}">{I['PHONE']} {PHONE}</a>
      </div>
      <ul class="hero-points">{pts}</ul>
    </div>
    {formhtml or ''}
  </div>
</section>
'''

def page_head(trail, h1, lead, eyebrow=None):
    eb = f'<span class="eyebrow">{esc(eyebrow)}</span>' if eyebrow else ''
    return f'<section class="page-head"><div class="wrap">{crumbs(trail)}{eb}<h1>{h1}</h1><p class="lead">{lead}</p></div></section>\n'

def trust(items):
    inner = ''.join(f'<div class="trust-item"><div class="ic">{I[ic]}</div><div>{a}<small>{b}</small></div></div>' for ic, a, b in items)
    return f'<section class="trust"><div class="wrap">{inner}</div></section>\n'

ARROW_SM = I['ARROW'].replace('<svg', '<svg style="width:16px;height:16px;vertical-align:-3px"')
def cards(eyebrow, h2, lead, items, cols=3, section_id='prestations', links=True):
    inner = ''
    for it in items:
        ic, tag, h, p = it[:4]; link = it[4] if len(it) > 4 else None
        tg = f'<span class="card-tag">{tag}</span>' if tag else ''
        more = f'<a class="more" href="{href(link)}">En savoir plus {ARROW_SM}</a>' if link and links else ''
        inner += f'<div class="card"><div class="ic">{I[ic]}</div>{tg}<h3>{h}</h3><p>{p}</p>{more}</div>'
    cls = 'services-grid' + (' cols4' if cols == 4 else ' cols2' if cols == 2 else '')
    return f'''<section class="section" id="{section_id}"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="{cls}">{inner}</div>
</div></section>
'''

def why(eyebrow, h2, lead, items):
    inner = ''.join(f'<div class="why-item"><div class="num">0{i+1}</div><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(items))
    return f'''<section class="section why"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="why-grid">{inner}</div>
</div></section>
'''

def approach(img, alt, badge, eyebrow, h2, lead, items, cta_text='Demander un devis gratuit', cta_href='/contact'):
    lis = ''.join(f'<li><span class="ck">{I["CK3"]}</span><div><strong>{a}</strong><span>{b}</span></div></li>' for a, b in items)
    return f'''<section class="section"><div class="wrap split">
  <div class="split-img">{pic(img, alt)}<div class="badge">{I['SHIELD0']} {badge}</div></div>
  <div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p>
    <ul class="check-list">{lis}</ul>
    <a class="btn btn-primary" href="{cta_href}">{cta_text}</a>
  </div>
</div></section>
'''

def process(h2, steps, eyebrow='Comment ça se passe'):
    inner = ''.join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a, b in steps)
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>
  <div class="steps">{inner}</div>
</div></section>
'''

def gallery(h2, items, eyebrow='Sur le terrain'):
    inner = ''.join(f'<figure>{pic(img, alt, card=True)}<figcaption>{cap}</figcaption></figure>' for img, alt, cap in items)
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>
  <div class="gallery">{inner}</div>
</div></section>
'''

def reviews(items, h2='Ce que disent nos clients', eyebrow='Avis Google'):
    inner = ''.join(f'<figure class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><blockquote>{esc(t)}</blockquote><figcaption>{esc(n)} · avis Google</figcaption></figure>' for n, t in items)
    return f'''<section class="section sand" id="avis"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">Extraits d'avis publiés sur notre fiche Google. <a href="{C.GBP_URL}" rel="noopener" target="_blank">Lire tous les avis</a>.</p></div>
  <div class="reviews">{inner}</div>
</div></section>
'''

def faq(items, h2='Ce que nos clients nous demandent', eyebrow='Questions fréquentes'):
    inner = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="section" id="faq"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>
  <div class="faq">{inner}</div>
</div></section>
'''

def cta(img, h2, lead):
    return f'''<section class="section cta">
  <picture><source type="image/webp" srcset="/img/w/{img}.webp"><img class="cta-bg" src="/img/{img}.jpg" alt="" loading="lazy" decoding="async"></picture>
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--yellow)">Parlons de votre arbre</span>
      <h2>{h2}</h2>
      <p class="lead">{lead}</p>
      <div class="cta-contact">
        <a href="tel:{PHONE_INTL}"><span class="ic">{I['PHONE']}</span><span>{PHONE}<small>Robin Humbert, arboriste-grimpeur</small></span></a>
        <a href="mailto:{EMAIL}"><span class="ic">{I['MAIL']}</span><span>{EMAIL}<small>Réponse sous 48 h ouvrées</small></span></a>
      </div>
    </div>
    <div><a class="btn btn-primary" href="/contact" style="font-size:1.1rem;padding:1.1rem 2rem">Demander mon devis gratuit {I['ARROW']}</a></div>
  </div>
</section>
'''

MAP_SVG = open('img/carte-zone.svg.html', encoding='utf-8').read() if os.path.exists('img/carte-zone.svg.html') else ''

def zone_block(h2='Jura, Neuchâtel, Bienne, Fribourg et Vaud', lead='Nous nous déplaçons chez vous pour la visite, qui reste offerte, dans tout l\'arc jurassien et jusqu\'au Léman.'):
    cols = ''
    for c in ['JU', 'NE', 'BE', 'FR', 'VD']:
        towns = sorted([x for x in COMMUNES if x['canton'] == c], key=lambda x: -(x.get('population') or 0))[:8]
        lis = ''.join(f'<li><a href="{href(t["slug"])}">{esc(t["nom"])}</a></li>' for t in towns)
        cols += f'<div class="zone-col"><h3>{I["PIN"]}<a href="{href(CANTON_SLUG[c])}" style="text-decoration:none">{esc(CANTON_NAME[c])}</a></h3><ul>{lis}<li><a href="{href(CANTON_SLUG[c])}">Toutes les communes →</a></li></ul></div>'
    return f'''<section class="section zone" id="zone"><div class="wrap">
  <div class="center"><span class="eyebrow">Zone d'intervention</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="zone-grid">{cols}</div>
  <p class="center" style="margin-top:1.5rem"><a class="btn btn-outline" href="/zone-intervention">Voir toute la zone d'intervention</a></p>
</div></section>
'''

def services_tiles(exclude=None, h2='Tout ce dont un arbre a besoin', lead='Un seul spécialiste pour l\'ensemble de la vie de vos arbres. Nous vous conseillons la bonne intervention, au bon moment.'):
    items = [(s['icon'], s.get('tag', ''), s['nav'], s['teaser'], s['slug']) for s in SERVICES if s['slug'] != exclude]
    return cards('Nos services', h2, lead, items, cols=3)

# ---------------- Pages fixes ----------------
def build_home():
    H = C.HOME
    p = hero('arboriste_grimpeur-19', '62% 30%', H['eyebrow'], H['h1'], H['lead'], H['points'], form('accueil'))
    p += trust(H['trust'])
    p += cards('Nos services', H['services_h2'], H['services_lead'], [(s['icon'], s.get('tag', ''), s['nav'], s['teaser'], s['slug']) for s in SERVICES], cols=3)
    p += why(*H['why'])
    p += approach(*H['approach'])
    p += process(H['process_h2'], H['process'])
    p += gallery('Nos interventions', H['gallery'])
    p += reviews(C.REVIEWS)
    p += zone_block()
    p += C.guides_teaser(GUIDES) if GUIDES else ''
    p += faq(H['faq'])
    p += cta('entretien_platanes_porrentruy', 'Un doute sur un arbre ? Demandez l\'avis d\'un professionnel.', 'Visite et devis gratuits, sans engagement. Nous vous répondons sous 48 h ouvrées.')
    ld = jsonld(business_jsonld(), {'@type': 'WebSite', 'name': BRAND, 'url': SITE, 'publisher': {'@id': BUSINESS_ID}}, faq_ld(H['faq']))
    write('index', head('index', H['title'], H['desc'], ld=ld, preload='arboriste_grimpeur-19') + header('index') + p + footer())
    register('index', '1.0')

def build_service(s):
    slug = s['slug']
    trail = [('Accueil', 'index'), ('Services', 'index#prestations'), (s['nav'], slug)]
    p = hero(s['hero_img'], s['hero_pos'], s['eyebrow'], s['h1'], s['lead'], s['points'], form(slug, s['form_title'], s['form_sub'], s['form_options']), trail=trail)
    p += trust(s['trust'])
    p += cards(s['cards_eyebrow'], s['cards_h2'], s['cards_lead'], s['cards'], cols=3)
    if s.get('why'): p += why(*s['why'])
    p += approach(*s['approach'])
    p += process(s['process_h2'], s['process'])
    if s.get('gallery'): p += gallery(s['gallery_h2'], s['gallery'])
    p += services_tiles(exclude=slug, h2='Nos autres services', lead='Taille, abattage, plantation, diagnostic : le même soin pour toutes les étapes de la vie de vos arbres.')
    p += zone_block()
    p += faq(s['faq'])
    p += cta(s['cta_img'], s['cta_h2'], s['cta_lead'])
    ld = jsonld({'@type': 'Service', 'name': s['nav'], 'serviceType': s['service_type'], 'provider': {'@id': BUSINESS_ID}, 'areaServed': business_jsonld()['areaServed'], 'url': url(slug), 'description': s['desc']}, breadcrumb_ld(trail[:1] + trail[2:]), faq_ld(s['faq']))
    write(slug, head(slug, s['title'], s['desc'], og_img=s['hero_img'], ld=ld, preload=s['hero_img']) + header(slug) + p + footer())
    register(slug, '0.9')

def build_b2b():
    B = C.B2B; slug = 'collectivites-entreprises'
    trail = [('Accueil', 'index'), ('Collectivités et entreprises', slug)]
    p = hero(B['hero_img'], B['hero_pos'], B['eyebrow'], B['h1'], B['lead'], B['points'], form(slug, B['form_title'], B['form_sub'], B['form_options']), trail=trail)
    p += cards(B['cards_eyebrow'], B['cards_h2'], B['cards_lead'], B['cards'], cols=3)
    p += approach(*B['approach'])
    p += process(B['process_h2'], B['process'])
    p += zone_block()
    p += faq(B['faq'])
    p += cta('abattage_arbre_porrentruy-6', B['cta_h2'], B['cta_lead'])
    ld = jsonld({'@type': 'Service', 'name': 'Entretien arboricole pour collectivités, gérances et entreprises', 'provider': {'@id': BUSINESS_ID}, 'url': url(slug)}, breadcrumb_ld(trail), faq_ld(B['faq']))
    write(slug, head(slug, B['title'], B['desc'], og_img=B['hero_img'], ld=ld, preload=B['hero_img']) + header(slug) + p + footer())
    register(slug, '0.8')

def build_about():
    A = C.ABOUT; slug = 'a-propos'
    trail = [('Accueil', 'index'), ('À propos', slug)]
    p = page_head(trail, A['h1'], A['lead'], 'À propos')
    p += f'<section class="section"><div class="wrap split"><div class="split-img">{pic(A["img"], A["img_alt"])}</div><div class="prose">{A["body"]}</div></div></section>\n'
    p += why(*A['values'])
    p += gallery('Quelques interventions', C.HOME['gallery'])
    p += cta('arboriste_grimpeur-2', 'Parlons de vos arbres', 'Une visite sur place pour comprendre votre situation, puis un devis écrit. Sans engagement.')
    ld = jsonld({'@type': 'AboutPage', 'name': A['title'], 'url': url(slug), 'about': {'@id': BUSINESS_ID}}, {'@type': 'Person', '@id': SITE + '#robin', 'name': 'Robin Humbert', 'jobTitle': 'Arboriste-grimpeur', 'worksFor': {'@id': BUSINESS_ID}, 'url': url(slug)}, breadcrumb_ld(trail))
    write(slug, head(slug, A['title'], A['desc'], og_img=A['img'], ld=ld) + header(slug) + p + footer())
    register(slug, '0.7')

def build_contact():
    slug = 'contact'; trail = [('Accueil', 'index'), ('Contact et devis', slug)]
    p = page_head(trail, 'Contact et <em class="hl">devis gratuit</em>', 'Décrivez votre arbre, nous vous rappelons pour convenir d\'une visite sur place. Devis écrit, sans engagement.', 'Contact')
    p += f'''<section class="section"><div class="wrap split" style="align-items:start">
  <div>
    <h2>Nous joindre</h2>
    <div class="cta-contact" style="color:var(--ink)">
      <a href="tel:{PHONE_INTL}" style="color:var(--green-900)"><span class="ic" style="background:var(--sand)">{I['PHONE']}</span><span>{PHONE}<small style="color:var(--muted)">Robin Humbert, arboriste-grimpeur · en français</small></span></a>
      <a href="mailto:{EMAIL}" style="color:var(--green-900)"><span class="ic" style="background:var(--sand)">{I['MAIL']}</span><span>{EMAIL}<small style="color:var(--muted)">Réponse sous 48 h ouvrées, en français ou en allemand</small></span></a>
      <a href="https://www.google.com/maps/search/?api=1&query=Derri%C3%A8re-Metthiez+13+2950+Courgenay" rel="noopener" target="_blank" style="color:var(--green-900)"><span class="ic" style="background:var(--sand)">{I['PIN']}</span><span>{ADDRESS['street']}, {ADDRESS['zip']} {ADDRESS['city']} (JU)<small style="color:var(--muted)">Siège de l'entreprise · interventions dans tout l'arc jurassien et jusqu'au Léman</small></span></a>
    </div>
    <div class="prose" style="margin-top:2rem">{C.CONTACT_BODY}</div>
  </div>
  {form('contact', 'Demande de devis', 'Nous revenons vers vous sous 48 h ouvrées pour fixer une visite.')}
</div></section>
'''
    p += zone_block()
    ld = jsonld({'@type': 'ContactPage', 'name': 'Contact et devis gratuit – Arboritaille', 'url': url(slug), 'about': {'@id': BUSINESS_ID}}, breadcrumb_ld(trail))
    write(slug, head(slug, 'Contact et devis gratuit – Arboriste-grimpeur | Arboritaille', 'Arboritaille, arboriste-grimpeur à Courgenay : devis gratuit pour la taille, l\'abattage ou la plantation d\'arbres. Jura, Neuchâtel, Bienne, Fribourg, Vaud.', ld=ld) + header(slug) + p + footer())
    register(slug, '0.8')

def build_simple(slug, title, desc, h1, lead, body, eyebrow=None, noindex=False, priority='0.3'):
    trail = [('Accueil', 'index'), (re.sub(r'<[^>]+>', '', h1), slug)]
    p = page_head(trail, h1, lead, eyebrow) + f'<section class="section"><div class="narrow prose article">{body}</div></section>\n'
    write(slug, head(slug, title, desc, noindex=noindex, ld=jsonld(breadcrumb_ld(trail))) + header(slug) + p + footer())
    if not noindex: register(slug, priority)

def build_merci():
    slug = 'merci'
    body = f'''<p>Nous vous recontactons sous 48 h ouvrées pour convenir d'une visite. Besoin d'une réponse plus rapide ? Appelez le <a href="tel:{PHONE_INTL}">{PHONE}</a>.</p>
<p>En attendant, nos <a href="/conseils">conseils</a> répondent aux questions les plus fréquentes : période de taille, autorisation d'abattage, prix.</p>
<p><a class="btn btn-primary" href="/">Retour à l'accueil</a></p>'''
    p = page_head([('Accueil', 'index'), ('Merci', slug)], 'Merci, votre demande est bien reçue', 'Votre message est arrivé chez Robin Humbert.') + f'<section class="section"><div class="narrow prose">{body}</div></section>\n'
    write(slug, head(slug, 'Merci – Demande envoyée | Arboritaille', 'Votre demande de devis est bien reçue.', noindex=True) + header() + p + footer())

def build_404():
    p = page_head([('Accueil', 'index'), ('Page introuvable', '404')], 'Page introuvable', 'Cette page n\'existe pas ou a été déplacée.') + '<section class="section"><div class="narrow prose"><p>Vous cherchiez peut-être : <a href="/elagage-taille-arbres">la taille et l\'élagage</a>, <a href="/abattage-demontage">l\'abattage</a>, <a href="/zone-intervention">notre zone d\'intervention</a> ou <a href="/conseils">nos conseils</a>.</p><p><a class="btn btn-primary" href="/">Retour à l\'accueil</a></p></div></section>\n'
    write('404', head('404', 'Page introuvable | Arboritaille', 'Page introuvable.', noindex=True) + header() + p + footer())

# ---------------- Zone, cantons, communes ----------------
def commune_link(c): return f'<a href="{href(c["slug"])}">{esc(c["nom"])}</a>'

def build_zone_hub():
    slug = 'zone-intervention'; trail = [('Accueil', 'index'), ('Zone d\'intervention', slug)]
    p = page_head(trail, 'Arboriste-grimpeur du Jura au Léman : <em class="hl">notre zone d\'intervention</em>', 'Depuis Courgenay, nous intervenons dans le canton du Jura, à Neuchâtel, à Bienne et dans le canton de Berne, dans le canton de Fribourg et dans le nord et le centre vaudois jusqu\'à Lausanne et la Riviera. La visite sur place reste offerte.', 'Zone d\'intervention')
    if MAP_SVG: p += f'<section class="section-sm"><div class="wrap"><div class="zone-map-box">{MAP_SVG}</div></div></section>\n'
    for c in ['JU', 'NE', 'BE', 'FR', 'VD']:
        cs = sorted([x for x in COMMUNES if x['canton'] == c], key=lambda x: x['nom'])
        by_d = {}
        for x in cs: by_d.setdefault(x.get('district') or '', []).append(x)
        cols = ''.join(f'<div class="zone-col"><h3>{I["PIN"]}{esc(d or CANTON_SHORT[c])}</h3><ul>' + ''.join(f'<li>{commune_link(x)}</li>' for x in xs) + '</ul></div>' for d, xs in sorted(by_d.items()))
        intro = CANTONS.get(c, {}).get('resume', '')
        p += f'<section class="section-sm"><div class="wrap"><h2><a href="{href(CANTON_SLUG[c])}" style="text-decoration:none;color:var(--green-900)">{esc(CANTON_NAME[c])}</a></h2><p class="lead">{intro}</p><div class="zone-grid">{cols}</div></div></section>\n'
    p += cta('arboriste_grimpeur-3', 'Votre commune n\'apparaît pas ?', 'Appelez-nous : nous nous déplaçons volontiers un peu plus loin pour une visite, selon le chantier.')
    ld = jsonld({'@type': 'CollectionPage', 'name': 'Zone d\'intervention – Arboritaille', 'url': url(slug), 'about': {'@id': BUSINESS_ID}}, breadcrumb_ld(trail))
    write(slug, head(slug, 'Zone d\'intervention – Communes et cantons | Arboritaille', 'Toutes les communes où Arboritaille intervient pour la taille, l\'abattage et la plantation d\'arbres : Jura, Neuchâtel, Bienne et Berne, Fribourg, Vaud.', ld=ld) + header(slug) + p + footer())
    register(slug, '0.8')

def build_canton(c):
    K = CANTONS.get(c)
    slug = CANTON_SLUG[c]; trail = [('Accueil', 'index'), ('Zone d\'intervention', 'zone-intervention'), (CANTON_NAME[c], slug)]
    cs = sorted([x for x in COMMUNES if x['canton'] == c], key=lambda x: x['nom'])
    big = sorted(cs, key=lambda x: -(x.get('population') or 0))[:6]
    if not K:
        K = {'title': f'Arboriste-grimpeur {CANTON_NAME[c]} | Arboritaille', 'desc': f'Taille, élagage, abattage et plantation d\'arbres dans le {CANTON_NAME[c]}.', 'h1': f'Arboriste-grimpeur dans le <em>{CANTON_NAME[c]}</em>', 'lead': '', 'points': C.HOME['points'], 'intro': '', 'contexte': [], 'reglement': '', 'faq': []}
    p = hero(K.get('hero_img', 'arboriste_grimpeur-3'), K.get('hero_pos', '50% 40%'), f'Arboriste-grimpeur · {CANTON_NAME[c]}', K['h1'], K['lead'], K['points'], form(slug, city_ph=', '.join(x['nom'] for x in big[:3]) + '…'), trail=trail)
    p += trust(C.HOME['trust'])
    if K.get('intro') or K.get('contexte'):
        ctx = ''.join(f'<div class="local-item"><h3>{I.get(x.get("icone", "TREE"), I["TREE"])}{esc(x["titre"])}</h3><p>{x["texte"]}</p></div>' for x in K.get('contexte', []))
        p += f'<section class="section"><div class="wrap"><div class="prose" style="max-width:76ch;margin-inline:auto"><span class="eyebrow">Vos arbres dans le {esc(CANTON_SHORT[c])}</span><h2>{esc(K.get("intro_h2", "Ce que nous rencontrons le plus souvent"))}</h2>{K.get("intro", "")}</div><div class="local-grid">{ctx}</div></div></section>\n'
    if K.get('reglement'):
        p += f'<section class="section-sm"><div class="narrow"><div class="notice"><strong>Autorisation d\'abattage et d\'élagage : {esc(CANTON_NAME[c])}.</strong> {K["reglement"]}</div></div></section>\n'
    p += services_tiles()
    by_d = {}
    for x in cs: by_d.setdefault(x.get('district') or '', []).append(x)
    cols = ''.join(f'<div class="zone-col"><h3>{I["PIN"]}{esc(d or CANTON_SHORT[c])}</h3><ul>' + ''.join(f'<li>{commune_link(x)}</li>' for x in xs) + '</ul></div>' for d, xs in sorted(by_d.items()))
    p += f'<section class="section zone"><div class="wrap"><div class="center"><span class="eyebrow">Communes</span><h2>Nos interventions dans le {esc(CANTON_SHORT[c])}, commune par commune</h2><p class="lead">{K.get("communes_lead", "Chaque page décrit les arbres, les contraintes et les règles propres à la commune.")}</p></div><div class="zone-grid">{cols}</div></div></section>\n'
    if K.get('faq'): p += faq([(q['q'], q['a']) for q in K['faq']])
    p += cta(K.get('cta_img', 'reduction_tilleul_porrentruy'), K.get('cta_h2', 'Un arbre à tailler ou à abattre ?'), K.get('cta_lead', 'Visite et devis gratuits, sans engagement. Réponse sous 48 h ouvrées.'))
    ld = [{'@type': 'Service', 'name': f'Arboriste-grimpeur – {CANTON_NAME[c]}', 'provider': {'@id': BUSINESS_ID}, 'areaServed': {'@type': 'AdministrativeArea', 'name': CANTON_NAME[c]}, 'url': url(slug)}, breadcrumb_ld(trail)]
    if K.get('faq'): ld.append(faq_ld([(q['q'], q['a']) for q in K['faq']]))
    write(slug, head(slug, K['title'], K['desc'], og_img=K.get('hero_img', 'arboriste_grimpeur-3'), ld=jsonld(*ld), preload=K.get('hero_img', 'arboriste_grimpeur-3')) + header('zone-intervention') + p + footer())
    register(slug, '0.8')

def build_commune(c):
    X = COMMUNE_CONTENT.get(c['slug'])
    if not X: return False
    slug = c['slug']; canton = c['canton']
    trail = [('Accueil', 'index'), ('Zone d\'intervention', 'zone-intervention'), (CANTON_NAME[canton], CANTON_SLUG[canton]), (c['nom'], slug)]
    p = hero(X.get('hero_img', 'arboriste_grimpeur-19'), X.get('hero_pos', '62% 30%'), X['eyebrow'], X['h1'], X['lead'], X['points'], form(slug, city_ph=c['nom']), trail=trail)
    facts = ''
    for lab, val in X.get('faits', []):
        facts += f'<div class="fact"><small>{esc(lab)}</small><strong>{esc(val)}</strong></div>'
    ctx = ''.join(f'<div class="local-item"><h3>{I.get(x.get("icone", "TREE"), I["TREE"])}{esc(x["titre"])}</h3><p>{x["texte"]}</p></div>' for x in X.get('contexte', []))
    p += f'''<section class="section"><div class="wrap">
  <div class="split" style="align-items:start"><div class="prose"><span class="eyebrow">{esc(X.get('intro_eyebrow', 'Vos arbres à ' + c['nom']))}</span><h2>{X['intro_h2']}</h2>{X['intro']}</div><div><div class="facts" style="grid-template-columns:repeat(2,1fr);margin-top:0">{facts}</div>{'<div class="notice" style="margin-top:1.25rem">' + X['reglement'] + '</div>' if X.get('reglement') else ''}</div></div>
  <div class="local-grid">{ctx}</div>
</div></section>
'''
    items = [(s['icon'], s.get('tag', ''), s['nav'], (X.get('services', {}) or {}).get(s['slug'], s['teaser']), s['slug']) for s in SERVICES]
    p += cards('Nos services à ' + esc(c['nom']), X.get('services_h2', f'Taille, abattage, plantation : nos interventions à {c["nom"]}'), X.get('services_lead', 'Chaque arbre est évalué sur place avant toute intervention. Devis écrit et gratuit.'), items, cols=3)
    p += process(X.get('process_h2', 'Quatre étapes, du premier contact au terrain propre'), C.HOME['process'])
    if X.get('galerie'): p += gallery(X.get('galerie_h2', 'Nos interventions'), X['galerie'])
    # communes voisines : même district, puis même canton
    same = [x for x in COMMUNES if x is not c and x['canton'] == canton and x.get('district') == c.get('district')]
    others = [x for x in COMMUNES if x is not c and x['canton'] == canton and x not in same]
    vois = (sorted(same, key=lambda x: -(x.get('population') or 0)) + sorted(others, key=lambda x: -(x.get('population') or 0)))[:12]
    chips = ''.join(f'<li>{commune_link(x)}</li>' for x in vois)
    p += f'<section class="section-sm zone"><div class="wrap"><span class="eyebrow">Autour de {esc(c["nom"])}</span><h2>Nous intervenons aussi dans les communes voisines</h2><ul class="chips">{chips}<li><a href="{href(CANTON_SLUG[canton])}">Tout le {esc(CANTON_SHORT[canton])} →</a></li></ul></div></section>\n'
    p += faq([(q['q'], q['a']) for q in X['faq']], h2=X.get('faq_h2', f'Questions fréquentes à {c["nom"]}'))
    p += cta(X.get('cta_img', 'entretien_platanes_porrentruy'), X.get('cta_h2', f'Un arbre à {c["nom"]} ? Demandez l\'avis d\'un professionnel.'), X.get('cta_lead', 'Visite et devis gratuits, sans engagement. Réponse sous 48 h ouvrées.'))
    ld = jsonld({'@type': 'Service', 'name': f'Arboriste-grimpeur à {c["nom"]}', 'serviceType': 'Taille, élagage, abattage et plantation d\'arbres', 'provider': {'@id': BUSINESS_ID}, 'areaServed': {'@type': 'City', 'name': c['nom'], 'containedInPlace': {'@type': 'AdministrativeArea', 'name': CANTON_NAME[canton]}}, 'url': url(slug), 'description': X['desc']}, breadcrumb_ld(trail), faq_ld([(q['q'], q['a']) for q in X['faq']]))
    write(slug, head(slug, X['title'], X['desc'], og_img=X.get('hero_img', 'arboriste_grimpeur-19'), ld=ld, preload=X.get('hero_img', 'arboriste_grimpeur-19')) + header('zone-intervention') + p + footer())
    register(slug, '0.7')
    return True

def build_ville_service(slug, X):
    """Page service × grande ville (ex. elagage-delemont)."""
    s = SERVICE_BY_SLUG[X['service']]; c = BY_SLUG[X['commune']]
    trail = [('Accueil', 'index'), (s['nav'], s['slug']), (X['h1_plain'], slug)]
    p = hero(X.get('hero_img', s['hero_img']), X.get('hero_pos', s['hero_pos']), X['eyebrow'], X['h1'], X['lead'], X['points'], form(slug, s['form_title'], s['form_sub'], s['form_options'], city_ph=c['nom']), trail=trail)
    p += trust(s['trust'])
    ctx = ''.join(f'<div class="local-item"><h3>{I.get(x.get("icone", "TREE"), I["TREE"])}{esc(x["titre"])}</h3><p>{x["texte"]}</p></div>' for x in X.get('contexte', []))
    notice = f'<div class="notice" style="max-width:76ch;margin:1.5rem auto 0">{X["reglement"]}</div>' if X.get('reglement') else ''
    p += f'<section class="section"><div class="wrap"><div class="prose" style="max-width:76ch;margin-inline:auto"><span class="eyebrow">{esc(X.get("intro_eyebrow", c["nom"]))}</span><h2>{X["intro_h2"]}</h2>{X["intro"]}</div><div class="local-grid">{ctx}</div>{notice}</div></section>\n'
    p += cards(s['cards_eyebrow'], s['cards_h2'], s['cards_lead'], s['cards'], cols=3)
    p += approach(*s['approach'])
    p += process(s['process_h2'], s['process'])
    p += f'<section class="section-sm zone"><div class="wrap"><span class="eyebrow">Voir aussi</span><h2>Nos autres interventions à {esc(c["nom"])}</h2><ul class="chips"><li><a href="{href(c["slug"])}">Arboriste-grimpeur à {esc(c["nom"])}</a></li>' + ''.join(f'<li><a href="{href(k)}">{esc(v["h1_plain"])}</a></li>' for k, v in VILLE_CONTENT.items() if v['commune'] == c['slug'] and k != slug) + f'<li><a href="{href(CANTON_SLUG[c["canton"]])}">{esc(CANTON_NAME[c["canton"]])}</a></li></ul></div></section>\n'
    p += faq([(q['q'], q['a']) for q in X['faq']], h2=X.get('faq_h2', f'Questions fréquentes à {c["nom"]}'))
    p += cta(X.get('cta_img', s['cta_img']), X.get('cta_h2', s['cta_h2']), X.get('cta_lead', s['cta_lead']))
    ld = jsonld({'@type': 'Service', 'name': X['h1_plain'], 'serviceType': s['service_type'], 'provider': {'@id': BUSINESS_ID}, 'areaServed': {'@type': 'City', 'name': c['nom']}, 'url': url(slug), 'description': X['desc']}, breadcrumb_ld(trail), faq_ld([(q['q'], q['a']) for q in X['faq']]))
    write(slug, head(slug, X['title'], X['desc'], og_img=X.get('hero_img', s['hero_img']), ld=ld, preload=X.get('hero_img', s['hero_img'])) + header(s['slug']) + p + footer())
    register(slug, '0.8')

# ---------------- Conseils (guides) ----------------
def render_sections(secs):
    out = ''
    for sec in secs:
        if sec.get('h2'): out += f'<h2 id="{slugify(sec["h2"])}">{esc(sec["h2"])}</h2>'
        if sec.get('h3'): out += f'<h3>{esc(sec["h3"])}</h3>'
        for para in sec.get('p', []): out += f'<p>{para}</p>'
        if sec.get('ul'): out += '<ul>' + ''.join(f'<li>{x}</li>' for x in sec['ul']) + '</ul>'
        if sec.get('ol'): out += '<ol>' + ''.join(f'<li>{x}</li>' for x in sec['ol']) + '</ol>'
        if sec.get('quote'): out += f'<blockquote>{sec["quote"]}</blockquote>'
        if sec.get('img'): out += f'<figure>{pic(sec["img"], sec.get("alt", ""))}<figcaption>{esc(sec.get("legende", ""))}</figcaption></figure>'
        if sec.get('notice'): out += f'<div class="notice">{sec["notice"]}</div>'
    return out

def build_guide(slug, G):
    trail = [('Accueil', 'index'), ('Conseils', 'conseils'), (G['titre_court'], 'conseils/' + slug)]
    toc = ''.join(f'<li><a href="#{slugify(s["h2"])}">{esc(s["h2"])}</a></li>' for s in G['sections'] if s.get('h2'))
    body = f'''<article class="article">
  {crumbs(trail)}
  <span class="eyebrow">{esc(G.get('categorie', 'Conseils'))}</span>
  <h1>{G['h1']}</h1>
  <p class="lead">{G['lead']}</p>
  <div class="article-meta"><span>Par Robin Humbert, arboriste-grimpeur</span><span>Mis à jour le {datetime.date.fromisoformat(G.get('date', TODAY)).strftime('%d.%m.%Y')}</span><span>{G.get('duree', '5')} min de lecture</span></div>
  {'<figure>' + pic(G['img'], G.get('img_alt', ''), lazy=False) + '</figure>' if G.get('img') else ''}
  <div class="toc"><strong>Au sommaire</strong><ol>{toc}</ol></div>
  {render_sections(G['sections'])}
  {('<div class="sources"><strong>Sources</strong><ul>' + ''.join(f'<li><a href="{esc(s["url"])}" rel="noopener nofollow" target="_blank">{esc(s["titre"])}</a></li>' for s in G['sources']) + '</ul></div>') if G.get('sources') else ''}
  <div class="author"><img src="/img/w/arboriste_grimpeur-15-800.webp" alt="" loading="lazy" width="64" height="64"><div><strong>Robin Humbert</strong><p>Arboriste-grimpeur, fondateur d'Arboritaille à Courgenay (JU). Taille raisonnée, abattage, démontage, plantation et diagnostic dans l'arc jurassien, à Fribourg et dans le canton de Vaud. <a href="/a-propos">En savoir plus</a></p></div></div>
</article>'''
    p = f'<section class="section"><div class="wrap">{body}</div></section>\n'
    if G.get('faq'): p += faq([(q['q'], q['a']) for q in G['faq']], h2='Questions fréquentes')
    rel = [k for k in GUIDES if k != slug][:3]
    p += f'<section class="section-sm sand"><div class="wrap"><span class="eyebrow">À lire aussi</span><h2>D\'autres conseils</h2><div class="services-grid" style="margin-top:1.5rem">' + ''.join(f'<a class="card card-link" href="/conseils/{k}"><h3>{esc(GUIDES[k]["titre_court"])}</h3><p>{esc(GUIDES[k]["lead"][:140])}…</p></a>' for k in rel) + '</div></div></section>\n'
    p += cta(G.get('cta_img', 'arboriste_grimpeur-2'), 'Une question sur votre arbre ?', 'Visite et devis gratuits. Nous vous conseillons au cas par cas, sans engagement.')
    ld = [{'@type': 'Article', 'headline': G['h1_plain'] if G.get('h1_plain') else re.sub(r'<[^>]+>', '', G['h1']), 'description': G['desc'], 'datePublished': G.get('date', TODAY), 'dateModified': G.get('date', TODAY), 'author': {'@type': 'Person', 'name': 'Robin Humbert', 'url': SITE + 'a-propos'}, 'publisher': {'@id': BUSINESS_ID}, 'image': SITE + 'img/' + G.get('img', 'arboriste_grimpeur-2') + '.jpg', 'mainEntityOfPage': url('conseils/' + slug), 'inLanguage': 'fr-CH'}, breadcrumb_ld(trail)]
    if G.get('faq'): ld.append(faq_ld([(q['q'], q['a']) for q in G['faq']]))
    write(slug, head('conseils/' + slug, G['title'], G['desc'], og_img=G.get('img', 'arboriste_grimpeur-2'), ld=jsonld(*ld)) + header('conseils') + p + footer(), subdir='conseils')
    register('conseils/' + slug, '0.7', G.get('date'))

def build_guides_hub():
    slug = 'conseils'; trail = [('Accueil', 'index'), ('Conseils', slug)]
    p = page_head(trail, 'Conseils d\'arboriste : <em class="hl">comprendre vos arbres</em>', 'Période de taille, autorisations, prix, arbres dangereux, plantation : les réponses d\'un arboriste-grimpeur aux questions que nos clients nous posent.', 'Conseils')
    items = ''.join(f'<a class="card card-link card-img" href="/conseils/{k}">{pic(g.get("img", "arboriste_grimpeur-2"), g.get("img_alt", ""), card=True)}<div class="card-body"><span class="card-tag">{esc(g.get("categorie", "Conseils"))}</span><h3>{esc(g["titre_court"])}</h3><p>{esc(g["lead"][:160])}…</p></div></a>' for k, g in GUIDES.items())
    p += f'<section class="section"><div class="wrap"><div class="services-grid" style="margin-top:0">{items}</div></div></section>\n'
    p += cta('arboriste_grimpeur-3', 'Un doute sur un arbre ?', 'Visite et devis gratuits, sans engagement.')
    write(slug, head(slug, 'Conseils d\'arboriste : taille, abattage, plantation | Arboritaille', 'Les conseils d\'un arboriste-grimpeur : quand tailler, faut-il une autorisation pour abattre, combien ça coûte, comment reconnaître un arbre dangereux, quel arbre planter.', ld=jsonld({'@type': 'CollectionPage', 'name': 'Conseils – Arboritaille', 'url': url(slug)}, breadcrumb_ld(trail))) + header(slug) + p + footer())
    register(slug, '0.7')

def build_sitemap_page():
    slug = 'plan-du-site'; trail = [('Accueil', 'index'), ('Plan du site', slug)]
    def ul(items): return '<ul>' + ''.join(f'<li><a href="{href(s)}">{esc(n)}</a></li>' for n, s in items) + '</ul>'
    body = '<h2>Services</h2>' + ul([(s['nav'], s['slug']) for s in SERVICES] + [('Collectivités et entreprises', 'collectivites-entreprises')])
    body += '<h2>Zone d\'intervention</h2>' + ul([('Toutes les communes', 'zone-intervention')] + [(CANTON_NAME[c], CANTON_SLUG[c]) for c in ['JU', 'NE', 'BE', 'FR', 'VD']])
    for c in ['JU', 'NE', 'BE', 'FR', 'VD']:
        body += f'<h3>{esc(CANTON_NAME[c])}</h3>' + ul([(x['nom'], x['slug']) for x in sorted(COMMUNES, key=lambda x: x['nom']) if x['canton'] == c and x['slug'] in COMMUNE_CONTENT])
    if VILLE_CONTENT: body += '<h2>Services par ville</h2>' + ul([(v['h1_plain'], k) for k, v in VILLE_CONTENT.items()])
    body += '<h2>Conseils</h2>' + ul([('Tous les conseils', 'conseils')] + [(g['titre_court'], 'conseils/' + k) for k, g in GUIDES.items()])
    body += '<h2>Entreprise</h2>' + ul([('À propos', 'a-propos'), ('Contact', 'contact'), ('Mentions légales', 'mentions-legales'), ('Protection des données', 'protection-des-donnees')])
    build_simple(slug, 'Plan du site | Arboritaille', 'Toutes les pages du site arboritaille.ch : services, pages cantons et communes, grandes villes, conseils et informations sur l\'entreprise.', 'Plan du site', 'Toutes les pages du site.', body, priority='0.2')

def build_files():
    urls = ''.join(f'<url><loc>{url(s)}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>' for s, lm, pr in PAGES)
    open('sitemap.xml', 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open('robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /contact.php\nDisallow: /tools/\nDisallow: /data/\nSitemap: {SITE}sitemap.xml\n')

# ---------------- Exécution ----------------
if __name__ == '__main__':
    for f in glob.glob('*.html') + glob.glob('conseils/*.html'): os.remove(f)
    build_home()
    for s in SERVICES: build_service(s)
    build_b2b(); build_about(); build_contact(); build_merci(); build_404()
    build_zone_hub()
    for c in ['JU', 'NE', 'BE', 'FR', 'VD']: build_canton(c)
    n = sum(1 for c in COMMUNES if build_commune(c))
    for k, v in VILLE_CONTENT.items(): build_ville_service(k, v)
    build_guides_hub()
    for k, g in GUIDES.items(): build_guide(k, g)
    build_simple('mentions-legales', 'Mentions légales | Arboritaille', 'Mentions légales du site arboritaille.ch : éditeur, raison individuelle Arboritaille, Humbert Robin, numéro IDE et hébergement.', 'Mentions légales', 'Éditeur du site et informations légales.', C.LEGAL)
    build_simple('protection-des-donnees', 'Protection des données | Arboritaille', 'Protection des données sur arboritaille.ch : données du formulaire de contact, durée de conservation, cookies de mesure et vos droits.', 'Protection des données', 'Ce que nous faisons de vos données, et les cookies utilisés.', C.PRIVACY)
    build_sitemap_page()
    build_files()
    print(f'OK : {len(PAGES)} pages indexables ({n} communes, {len(VILLE_CONTENT)} pages ville-service, {len(GUIDES)} conseils).')
