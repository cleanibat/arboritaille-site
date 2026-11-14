# arboritaille.ch — site principal (statique, SEO)

Site d'Arboritaille (Robin Humbert, arboriste-grimpeur, Courgenay JU). Généré en Python, hébergé sur IONOS, aperçu sur GitHub Pages.

## Génération

```bash
python3 build.py                 # génère les .html à la racine + conseils/, sitemap.xml, robots.txt
python3 tools/validate_content.py content   # contrôle des contenus JSON (faits, vocabulaire, similarité)
python3 tools/make_preview.py    # copie dans docs/ pour l'aperçu GitHub Pages (noindex, chemins préfixés)
python3 tools/serve.py 8766      # serveur local avec URL propres (comme .htaccess)
```

- `build.py` : moteur (gabarit, composants, JSON-LD, sitemap). `content_static.py` : textes des pages fixes (accueil, 7 services, B2B, à propos, contact, légal).
- `content/communes/<slug>.json` : une fiche par commune (248). `content/villes/` : pages service × grande ville. `content/cantons.json` : hubs cantonaux. `content/guides/` : articles conseils. Schémas et règles dans `content/SPEC.md`.
- `data/` : listes de communes (Wikipédia/OFS), faits par commune (`fetch_facts.py`, ignoré par git), briefs par lot (`make_briefs.py`), règles cantonales vérifiées (`reglements_cantons.json`), dossiers de recherche.
- URL propres via `.htaccess` (`/contact` → `contact.html`), redirections des anciennes adresses Hostinger, 404 personnalisée.

## Formulaire et CRM

`contact.php` : envoi e-mail (destinataire contact@arboritaille.ch, copie cachée agence), CSV et configuration Make dans `../prive_arboritaille/` hors docroot (`agence_arboritaille.json` : `make_url`, `client`, `cle`). Le champ `Origine` (Site / SEO / Google Ads / Meta Ads) alimente la colonne Source du CRM. Jamais de service tiers type FormSubmit.

## Déploiement

`.github/workflows/deploy-ssh.yml` : rsync vers IONOS à chaque push sur `main`, actif quand la variable de dépôt `DEPLOY` vaut `on` (secrets SSH_HOST, SSH_PORT, SSH_USER, SSH_KEY, SSH_KNOWN_HOSTS, SSH_TARGET_DIR, SITE_URL). Les fichiers de travail (`data/`, `tools/`, `content/`, `docs/`, `*.py`) ne sont pas publiés.

Aperçu : https://cleanibat.github.io/arboritaille-site/ (dossier `docs/`, formulaire désactivé, noindex).

## Suivi

GTM `GTM-WMF2BV3S` avec Mode Consentement v2 (bandeau maison dans `main.js`, choix conservé 6 mois). Aucun script de suivi maison.
