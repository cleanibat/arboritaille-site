# Cahier des charges rédaction — arboritaille.ch

Site statique généré par `build.py` à partir de fichiers JSON. Vous écrivez des JSON, pas du HTML de page.
Client : **Arboritaille, Robin Humbert, arboriste-grimpeur**, Derrière-Metthiez 13, 2950 Courgenay (JU), 078 306 53 04, contact@arboritaille.ch. Entreprise individuelle fondée en 2024. Travaille seul (dire « nous », jamais « notre équipe »). Clients : particuliers, entreprises, gérances, collectivités. Zone : canton du Jura, canton de Neuchâtel, Bienne et canton de Berne francophone, canton de Fribourg, nord et centre vaudois jusqu'à Lausanne et la Riviera (plus Soleure et Bâle à 15 km). Visite et devis gratuits, réponse sous 48 h ouvrées. Réponses écrites possibles en allemand.

Services (slugs des pages, à lier avec `/<slug>`) :
`elagage-taille-arbres` (taille et élagage), `abattage-demontage`, `urgence-tempete-arbre-dangereux`, `rognage-souche`, `haubanage`, `plantation-arbres`, `diagnostic-expertise-arbre`, `collectivites-entreprises`, `zone-intervention`, `contact`, `a-propos`, `conseils`.
Pages cantons : `arboriste-canton-du-jura`, `arboriste-canton-de-neuchatel`, `arboriste-bienne-canton-de-berne`, `arboriste-canton-de-fribourg`, `arboriste-canton-de-vaud`.
Pages communes : `arboriste-<slug>` (slug donné dans le brief). Guides : `/conseils/<slug>`.

## Règles d'écriture (vérifiées par `tools/validate_content.py`, à lancer avant de rendre)

1. **Faits uniquement.** Tout fait local vient du brief (`data/briefs/lot_XX.json` : population, altitude, superficie, district, localités, voisins, intro et sections Wikipédia, distance depuis Courgenay) ou de `data/reglements_cantons.json`. Rien d'autre : pas d'essence « typique » inventée, pas de « nombreux tilleuls » si le brief ne le dit pas. Vous pouvez raisonner à partir de faits (altitude 1000 m → hivers longs, épicéas et érables fréquents en montagne jurassienne ; vieux village avec vergers mentionnés → fruitiers haute-tige ; quartiers de villas → arbres de jardin près des maisons), en le formulant comme un raisonnement général (« à cette altitude… », « dans les quartiers de villas… »), jamais comme un constat de terrain.
2. **Aucune intervention passée inventée.** Nous n'avons de photos/interventions documentées qu'à Porrentruy, Neuchâtel, Bienne, Port (BE) et Courgenay. Ailleurs : jamais « nous avons déjà », « nous intervenons régulièrement à », « nos clients de X ».
3. **Aucun avis, certification, diplôme, ancienneté, nombre de clients, délai garanti.** Interdits : certifié, brevet, diplômé, membre de, ASSA, ISA, « depuis N ans », « N ans d'expérience », « sous 24 h », « 24h/24 », « 7j/7 », « garanti ».
4. **Aucun superlatif ni auto-promotion** : meilleur, n°1, leader, référence, expert reconnu, incontournable, exceptionnel, unique, imbattable, excellence, haut de gamme, premium, parfait, 100 %.
5. **Vocabulaire imposé** : « machines » (jamais « engins ») ; « Berne » ou « canton de Berne » (jamais « Jura bernois ») ; jamais « sans nacelle », « dans la région », « entreprise locale », « basé(s) à », « toute la Suisse romande », « proche de chez vous ». Dire « depuis Courgenay », « à une trentaine de kilomètres de Courgenay ». Les distances du brief sont à vol d'oiseau : écrire « env. 30 km » dans les faits, et en prose « à une trentaine de kilomètres de Courgenay » ou « à moins de dix kilomètres de Courgenay ». Tutoiement interdit, pas de point d'exclamation.
6. **Format court et visuel** : paragraphes ≤ 40 mots, une idée par phrase, pas de pavé. HTML autorisé dans `intro`, `reglement`, réponses FAQ, textes de contexte : `<p>`, `<a href="/…">`, `<strong>`, `<em>`, `<br>`, `<ul><li>`. Liens internes uniquement vers les slugs listés ci-dessus ou donnés dans le brief (voisins avec `slug` non nul) ; liens externes seulement vers des sources officielles (commune, canton, fedlex) et seulement dans `reglement` ou les guides.
7. **Unicité réelle.** Chaque page doit apprendre quelque chose de propre à la commune : relief, altitude, rivière, forêt, vergers, patrimoine bâti, type d'habitat, bilinguisme, distance. Le validateur rejette les intros trop semblables entre communes (similarité > 0,55). Variez la structure des phrases, l'angle d'attaque (sécurité, patrimoine, climat, voisinage, autorisation), l'ordre des blocs. Ne recopiez pas les phrases de l'exemple.
8. **Nom de la commune** dans `title`, `h1`, `desc`, `lead`, `intro` (au moins une fois), au moins deux questions de FAQ. Pas de liste de communes voisines dans un paragraphe (les voisins sont ajoutés automatiquement par le générateur sous forme de liens) : vous pouvez citer 1 ou 2 voisins dans une phrase si c'est utile (« comme à Porrentruy, voisine »).
9. **Réglementation** : reprendre `court` ou `resume` du canton dans `data/reglements_cantons.json`, éventuellement raccourci, et ajouter la règle communale seulement si elle figure dans `communes_connues`. Ne jamais inventer un seuil, une autorité ou un formulaire. Toujours finir par « Nous vérifions la règle de votre commune avant d'intervenir. » ou équivalent.
10. **Longueurs** : `title` 50-70 caractères avec « | Arboritaille » à la fin ; `desc` 120-160 caractères ; `lead` ≤ 40 mots ; `intro` 2 à 4 paragraphes ; `faq` 4 à 5 questions, réponses 25-60 mots.

Icônes disponibles (`icone`) : TREE, LEAF, MOUNT, HOME, WIND, WARN, SHIELD, PIN, CLOCK, USERS, SPROUT, DOC, SEARCH, CABLE, STUMP, AXE, SCISS, CRANE.
Photos disponibles (`hero_img`, `cta_img`, `img`) : arboriste_grimpeur-19 (grimpeur dans un grand arbre, défaut), arboriste_grimpeur-2 (grimpeur dans la couronne), arboriste_grimpeur-3 (cèdre, lac de Neuchâtel), arboriste_grimpeur-15 (feuillage), reduction_tilleul_porrentruy, entretien_platanes_porrentruy, demontage_arbre_porrentruy, demontage_d-arbre_retention, abattage_arbre_porrentruy-6 (grue), abattage_arbre_porrentruy-3 (tronc débité), abattage_sequoia (souche), demontage_saule_bienne, demontage_saule_port, plantation_arbre (tuteurage tripode, Neuchâtel), degagement_facade_epicea. Choisir une photo cohérente avec le canton quand c'est possible (lac de Neuchâtel pour le Littoral, saule de Bienne pour Bienne/Nidau…), sinon une photo générique de grimpe. Les légendes des photos doivent rester vraies (une photo prise à Porrentruy reste « Porrentruy »).

## Schéma d'une page commune — `content/communes/<slug>.json`

```json
{
 "title": "Arboriste-grimpeur à Alle (JU) : taille, abattage, soins aux arbres | Arboritaille",
 "desc": "120-160 caractères, avec le nom de la commune, le canton, 2-3 services et « visite et devis gratuits ».",
 "hero_img": "arboriste_grimpeur-19", "hero_pos": "62% 30%",
 "eyebrow": "Arboriste-grimpeur · Alle · Ajoie",
 "h1": "Arboriste-grimpeur à <em>Alle</em> : taille, abattage et soins aux arbres",
 "lead": "≤ 40 mots, situe la commune et ce que nous faisons.",
 "points": ["4 puces courtes", "…", "…", "…"],
 "intro_eyebrow": "Vos arbres à Alle",
 "intro_h2": "Titre H2 propre à la commune",
 "intro": "<p>…</p><p>…</p><p>…</p>",
 "faits": [["Habitants", "1 965 (2025)"], ["Altitude", "450 m"], ["District", "Porrentruy"], ["Depuis Courgenay", "env. 5 km"]],
 "reglement": "<strong>Autorisation d'abattage à Alle.</strong> Texte cantonal (court), règle communale si connue, phrase de vérification.",
 "contexte": [{"icone": "MOUNT", "titre": "…", "texte": "≤ 40 mots"}, {"icone": "HOME", "titre": "…", "texte": "…"}, {"icone": "LEAF", "titre": "…", "texte": "…"}],
 "services": {"elagage-taille-arbres": "teaser adapté ≤ 30 mots (facultatif, 2 à 7 services)", "abattage-demontage": "…"},
 "services_h2": "facultatif", "services_lead": "facultatif",
 "faq": [{"q": "…", "a": "…"}, {"q": "…", "a": "…"}, {"q": "…", "a": "…"}, {"q": "…", "a": "…"}],
 "cta_img": "entretien_platanes_porrentruy", "cta_h2": "…", "cta_lead": "…"
}
```
`faits` : 4 paires exactement, valeurs tirées du brief (population arrondie telle quelle, altitude, district ou NPA ou superficie, distance). Si le brief n'a pas de distance, remplacer par la superficie.
`galerie` : uniquement pour Porrentruy, Neuchâtel, Bienne, Port (photos réelles), format `[["nom_photo", "alt", "légende"], …]`.

## Schéma d'une page service × ville — `content/villes/<page-slug>.json`

Nom de fichier : `elagage-<slug-ville>.json` ou `abattage-arbre-<slug-ville>.json` (slug-ville = slug de la commune sans « arboriste- »).
```json
{
 "service": "elagage-taille-arbres", "commune": "arboriste-delemont",
 "h1_plain": "Élagage et taille d'arbres à Delémont",
 "title": "Élagage et taille d'arbres à Delémont (JU) | Arboritaille", "desc": "…",
 "eyebrow": "Élagage · Delémont", "h1": "Élagage et taille d'arbres à <em>Delémont</em>", "lead": "…", "points": ["…", "…", "…", "…"],
 "intro_eyebrow": "Delémont", "intro_h2": "…", "intro": "<p>…</p><p>…</p>",
 "contexte": [{"icone": "HOME", "titre": "…", "texte": "…"}, {"icone": "WARN", "titre": "…", "texte": "…"}, {"icone": "DOC", "titre": "…", "texte": "…"}],
 "reglement": "…",
 "faq": [{"q": "…", "a": "…"} × 4-5],
 "cta_h2": "…", "cta_lead": "…"
}
```
Pour `abattage-arbre-*` : `"service": "abattage-demontage"`. Le reste de la page (prestations, méthode, étapes) est ajouté automatiquement depuis la page service : n'y revenez pas, concentrez-vous sur ce qui est propre à la ville (quartiers, type d'habitat, règlement, accès, voisinage, période).

## Schéma des pages cantons — `content/cantons.json` (un objet par code JU/NE/BE/FR/VD)

```json
{"JU": {
 "title": "Arboriste-grimpeur dans le canton du Jura : taille, abattage, soins aux arbres | Arboritaille", "desc": "…",
 "h1": "Arboriste-grimpeur dans le <em>canton du Jura</em>", "lead": "…", "points": ["…", "…", "…", "…"],
 "hero_img": "reduction_tilleul_porrentruy", "hero_pos": "50% 40%",
 "resume": "1 phrase pour la page zone d'intervention",
 "intro_h2": "…", "intro": "<p>…</p><p>…</p><p>…</p>",
 "contexte": [{"icone": "MOUNT", "titre": "…", "texte": "…"} × 3-4],
 "reglement": "texte cantonal `resume` (complet) + phrase de vérification",
 "communes_lead": "…", "faq": [{"q": "…", "a": "…"} × 5], "cta_img": "…", "cta_h2": "…", "cta_lead": "…"
}}
```

## Schéma d'un guide — `content/guides/<slug>.json`

```json
{
 "title": "… | Arboritaille", "desc": "…", "titre_court": "pour les menus (≤ 45 caractères)", "categorie": "Taille",
 "h1": "…", "h1_plain": "…", "lead": "…", "date": "2026-11-11", "duree": 6,
 "img": "arboriste_grimpeur-2", "img_alt": "…",
 "sections": [{"h2": "…", "p": ["…", "…"], "ul": ["…"], "ol": ["…"], "h3": "…", "notice": "…", "quote": "…"}],
 "faq": [{"q": "…", "a": "…"}],
 "sources": [{"titre": "…", "url": "https://…"}]
}
```
Guides : 900 à 1 500 mots, structure H2 claire, chaque affirmation réglementaire ou scientifique sourcée (fedlex, sites cantonaux, WSL, Agroscope, BirdLife, ouvrages cités avec auteur et titre). Pas de chiffre de prix inventé : si une fourchette est donnée, elle vient d'une source publique suisse citée et est présentée comme un ordre de grandeur, pas comme nos tarifs. Terminer par une section « Ce que nous proposons » avec des liens vers 2-3 pages services.
