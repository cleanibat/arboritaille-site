# -*- coding: utf-8 -*-
"""Textes des pages fixes du site arboritaille.ch.
Règles : pas de superlatifs, pas d'avis ni de certification inventés, « machines » (pas « engins »),
paragraphes courts (≤ 40 mots), une idée par élément. Les textes des pages Taille et Abattage
reprennent ceux validés sur les landing pages Google Ads (page.arboritaille.ch)."""

PHONE_INTL = '+41783065304'; PHONE = '078 306 53 04'

# Profils publics réels de l'entreprise (recherche du 11.11.2026)
SAME_AS = [
    'https://www.facebook.com/p/Arboritaille-61594020257295/',
    'https://www.google.com/maps?cid=15461798967485162516',
    'https://www.local.ch/fr/d/courgenay/2950/arboriculture/arboritaille-gMcNk4YQmHDsPArWfadE1A',
    'https://search.ch/tel/courgenay/derriere-metthiez-13/arboritaille.fr.html',
]
GBP_URL = 'https://www.google.com/maps?cid=15461798967485162516'

FORM_OPTIONS = ["Taille et entretien", "Abattage ou démontage", "Diagnostic / expertise d'un arbre", "Plantation",
                "Haubanage / consolidation", "Rognage de souche", "Arbre dangereux / urgence", "Je ne sais pas encore, j'ai besoin d'un conseil"]

TRUST = [('SHIELD', "Arboriste-grimpeur", "Techniques de grimpe et cordes"),
         ('LEAF', "Respect de l'arbre", "Taille raisonnée, conseil sur mesure"),
         ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")]

PROCESS = [("Vous nous contactez", "Par le formulaire ou par téléphone. Quelques mots sur votre arbre suffisent."),
           ("Visite et diagnostic", "Nous venons voir l'arbre, écoutons vos attentes et vous conseillons la bonne intervention."),
           ("Devis clair et gratuit", "Un devis écrit et détaillé. Vous décidez librement."),
           ("Intervention et nettoyage", "Nous intervenons à la date convenue et laissons votre terrain propre.")]

GALLERY = [("arboriste_grimpeur-3", "Arboriste-grimpeur au sommet d'un cèdre, lac de Neuchâtel en arrière-plan", "Taille en hauteur, Neuchâtel"),
           ("reduction_tilleul_porrentruy", "Tilleul après réduction de couronne à Porrentruy", "Réduction d'un tilleul, Porrentruy"),
           ("demontage_arbre_porrentruy", "Démontage d'un grand arbre à Porrentruy", "Démontage tronçon par tronçon, Porrentruy"),
           ("demontage_saule_bienne", "Arboriste-grimpeur démontant un saule à Bienne", "Démontage d'un saule, Bienne"),
           ("plantation_arbre", "Jeune arbre planté avec tuteurage tripode à Neuchâtel", "Plantation et tuteurage tripode, Neuchâtel"),
           ("abattage_arbre_porrentruy-6", "Grue lors d'un abattage", "Levage à la grue en zone urbaine")]

# Avis Google réels (fiche « Arboritaille », 12 avis, 5,0/5 au 11.11.2026). Extraits tels que publiés.
REVIEWS = [
    ("Camille L.", "Élagage d'un vieux tilleul : travail bien fait, respect de la forme de l'arbre. Nettoyage après travaux impeccable."),
    ("Florian J.", "Contact chaleureux, devis rapide et intervention dans les 4 semaines. Prix absolument concurrentiel."),
    ("M. N.", "Un professionnel de confiance, passionné et rigoureux ! Robin Humbert est intervenu pour la sécurisation d'un grand frêne dans notre parc."),
    ("Marie-Noëlle G.", "Magnifique travail, beaucoup de sensibilité dans la taille de mes arbres."),
]

# ---------------------------------------------------------------- Accueil
HOME = dict(
    title="Arboriste-grimpeur à Courgenay (JU) – Taille, abattage | Arboritaille",
    desc="Arboriste-grimpeur à Courgenay (JU) : taille, élagage, abattage, souches, plantation et diagnostic. Devis gratuit dans le Jura, à Neuchâtel, Bienne, Fribourg et Vaud.",
    eyebrow="Arboriste-grimpeur · Jura · Neuchâtel · Bienne · Fribourg · Vaud",
    h1="Votre arboriste-grimpeur <em>pour tous les soins</em> de vos arbres",
    lead="Taille, élagage, abattage, démontage, diagnostic, plantation : Arboritaille prend soin de vos arbres avec les techniques de grimpe, les moyens adaptés à chaque situation et le respect du vivant. Pour les particuliers, les entreprises et les collectivités.",
    points=["Devis gratuit et sans engagement", "Réponse sous 48 h ouvrées", "Un seul interlocuteur, du conseil au chantier", "Chantier propre, branches évacuées"],
    trust=TRUST,
    services_h2="Tout ce dont un arbre a besoin, de la plantation à l'abattage",
    services_lead="Un seul spécialiste pour l'ensemble de la vie de vos arbres. Nous vous conseillons la bonne intervention, au bon moment.",
    why=("Pour qui", "Particuliers, entreprises, collectivités : le même soin, adapté à vos enjeux",
         "Que vous ayez un arbre dans votre jardin ou un parc d'arbres à gérer, vous avez le même besoin : un professionnel qui vous conseille selon votre situation.",
         [("Particuliers", "Entretien de vos arbres de jardin, mise en sécurité, abattage d'un sujet gênant. Devis gratuit et conseils personnalisés."),
          ("Entreprises", "Un arbre gêne votre chantier ou nécessite des soins ? Nous évaluons rapidement et intervenons sans tarder."),
          ("Collectivités", "Suivi de groupes d'arbres, gestion des sujets dangereux, projets de plantation. Un partenaire pour l'entretien arboricole communal."),
          ("Gérances et régies", "Entretien régulier du patrimoine arboré de vos immeubles, avec un interlocuteur unique et des devis clairs.")]),
    approach=("arboriste_grimpeur-2", "Arboriste-grimpeur dans la couronne d'un grand arbre", "Grimpe, nacelle ou grue selon le cas",
              "Notre approche", "La passion du métier, le respect du vivant",
              "Chaque arbre est un cas particulier. Avant d'intervenir, nous prenons le temps de le comprendre : son essence, sa vigueur, son environnement et ce que vous en attendez.",
              [("Un conseil sur mesure", "L'objectif est d'embellir et de conserver les arbres. Chaque situation est différente, parfois l'abattage est nécessaire. Nous sommes là pour vous conseiller."),
               ("Les bons moyens pour chaque arbre", "Grimpe à la corde par défaut, pour préserver votre jardin. Nacelle, grue ou autres machines quand la situation l'exige, et hélicoptère quand aucun autre accès n'est possible."),
               ("Des coupes propres et raisonnées", "Taille raisonnée et respect de la physiologie de l'arbre pour un résultat durable."),
               ("Un chantier rendu propre", "Branches broyées ou évacuées, bois débité si vous le souhaitez, terrain nettoyé.")],
              "Demander un devis gratuit"),
    process_h2="Quatre étapes, du premier contact au terrain propre",
    process=PROCESS,
    gallery=GALLERY,
    faq=[("Comment savoir si mon arbre a besoin d'une intervention ?", "Bois mort dans la couronne, branches qui touchent une toiture, champignons au pied, tronc penché ou fissuré, feuillage clairsemé : autant de signes à ne pas ignorer. Une visite gratuite permet de trancher."),
         ("Combien coûtent vos prestations ?", "Chaque arbre est différent : hauteur, essence, accès, type d'intervention et évacuation du bois font varier le prix. C'est pourquoi nous nous déplaçons gratuitement pour établir un devis écrit et précis."),
         ("Faut-il une autorisation pour tailler ou abattre un arbre ?", "Une taille d'entretien ne nécessite en général aucune démarche. L'abattage, ou une intervention sur un arbre protégé, peut être soumis à autorisation communale. Nous vous guidons dans la démarche. <a href=\"/conseils/autorisation-abattage-arbre\">Lire notre guide par canton</a>."),
         ("Mon arbre est difficile d'accès. Est-ce un problème ?", "Non. Nous travaillons en grimpe, à la corde, ce qui permet d'accéder aux jardins clos, terrains en pente et cours intérieures. Quand c'est nécessaire, nous mobilisons une nacelle, une grue ou d'autres machines, et dans des cas très particuliers un hélicoptère."),
         ("Dans quelle zone intervenez-vous ?", "Dans le canton du Jura, à Neuchâtel, Bienne, Soleure et Bâle, dans le canton de Fribourg et dans le canton de Vaud, d'Yverdon à Lausanne et à la Riviera. La visite sur place reste offerte. <a href=\"/zone-intervention\">Voir toutes les communes</a>."),
         ("Travaillez-vous avec les entreprises et les communes ?", "Oui. Nous accompagnons les entreprises sur leurs chantiers et les collectivités pour la gestion de leur patrimoine arboré : suivi, sécurité, plantations. <a href=\"/collectivites-entreprises\">Nos prestations pour les professionnels</a>.")],
)

# ---------------------------------------------------------------- Services
TAILLE = dict(
    slug='elagage-taille-arbres', nav="Taille et élagage", nav_sub="Entretien, réduction, sécurité", icon='SCISS', tag="Le plus demandé",
    teaser="Taille d'entretien, réduction ou rehaussement de couronne, suppression du bois mort. Une taille raisonnée qui respecte la forme et la santé de l'arbre.",
    service_type="Taille et élagage d'arbres",
    title="Taille et élagage d'arbres – Arboriste-grimpeur | Arboritaille",
    desc="Taille raisonnée et élagage de vos arbres par un arboriste-grimpeur. Visite et devis gratuits dans le Jura, à Neuchâtel, Bienne, Fribourg et Vaud.",
    hero_img='arboriste_grimpeur-19', hero_pos='62% 30%', eyebrow="Taille et élagage · Arboriste-grimpeur",
    h1="Taille et entretien d'arbres <em>dans les règles de l'art</em>",
    lead="Un arboriste-grimpeur professionnel prend soin de vos arbres : taille raisonnée, mise en sécurité, allègement de couronne, bois mort. En grimpe, en nacelle ou avec les machines adaptées, avec un devis clair et gratuit.",
    points=["Devis gratuit et sans engagement", "Réponse sous 48 h ouvrées", "Taille raisonnée, respectueuse de l'arbre", "Chantier propre, branches évacuées"],
    form_title="Recevez votre devis gratuit", form_sub="Décrivez-nous votre arbre en 30 secondes. Nous vous rappelons pour fixer une visite.",
    form_options=["Taille d'entretien", "Réduction ou allègement de couronne", "Élagage de sécurité (bois mort, branches dangereuses)", "Taille de fruitiers", "Diagnostic / conseil sur un arbre", "Abattage ou démontage", "Autre"],
    trust=[('SHIELD', "Arboriste-grimpeur", "Techniques de grimpe et cordes"), ('LEAF', "Taille raisonnée", "Respect de la physiologie de l'arbre"), ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")],
    cards_eyebrow="Nos prestations de taille", cards_h2="Chaque arbre mérite la taille qui lui convient",
    cards_lead="Il n'existe pas de taille standard. Nous observons l'arbre, son essence, son âge et son environnement avant de choisir l'intervention adaptée.",
    cards=[('CUT', "Le plus demandé", "Taille d'entretien", "Suppression du bois mort et des branches qui se croisent ou frottent, pour laisser passer la lumière et l'air. L'arbre garde sa silhouette naturelle."),
           ('SHRINK', "", "Réduction et allègement de couronne", "Pour un arbre devenu trop volumineux, trop proche d'une toiture ou d'une ligne. Nous réduisons de manière ciblée en limitant la taille des coupes pour impacter le moins possible la structure de l'arbre."),
           ('LIFT', "", "Rehaussement de couronne", "Remontée des branches basses pour dégager un passage, une façade, un accès véhicule ou une vue, tout en respectant les besoins de l'arbre."),
           ('WARN', "Urgence possible", "Élagage de sécurité", "Branches fissurées, bois mort au-dessus d'une zone de passage, arbre fragilisé après une tempête. Nous sécurisons rapidement et proprement."),
           ('PLUS', "", "Taille de formation", "Pour les jeunes arbres et les plantations récentes : guider la structure dès les premières années évite les gros travaux plus tard."),
           ('CABLE', "", "Haubanage et consolidation", "Quand une fourche ou une charpentière présente une faiblesse, un haubanage dynamique permet souvent de conserver l'arbre plutôt que de l'abattre.")],
    why=("Pourquoi faire tailler ses arbres", "Une taille bien faite protège vos arbres, vos biens ainsi que votre sécurité.",
         "Faire suivre vos arbres par un professionnel permet de prévenir les risques, de les adapter au mieux à leur environnement et ainsi de réduire au minimum les impacts subis, dans le but de les conserver le plus longtemps possible.",
         [("Sécurité", "Élimination du bois mort et des branches à risque au-dessus des toitures, terrasses, routes et aires de jeux."),
          ("Santé de l'arbre", "Des coupes propres, au bon endroit et de la plus petite taille possible, limitent champignons et parasites."),
          ("Lumière et espace", "Retrouvez de la clarté dans le jardin et la maison, dégagez une vue ou un passage sans sacrifier l'arbre."),
          ("Valeur du bien", "Des arbres sains et bien conduits valorisent votre propriété et vous évitent un abattage coûteux dans quelques années.")]),
    approach=("arboriste_grimpeur-2", "Arboriste-grimpeur en intervention dans la couronne d'un grand arbre", "Grimpe, nacelle ou grue selon le cas",
              "Notre approche", "La taille raisonnée : intervenir ni trop, ni trop peu",
              "Un arbre étêté ou taillé trop sévèrement s'affaiblit, produit des rejets fragiles et devient plus dangereux qu'avant. Nous faisons l'inverse.",
              [("Diagnostic avant de couper", "Essence, vigueur, défauts mécaniques, contraintes du terrain : chaque intervention commence par une lecture de l'arbre."),
               ("Des coupes propres, au bon endroit", "Respect du col de la branche et des proportions : l'arbre tolère mieux ce type de coupe."),
               ("Le bon moyen d'accès pour chaque arbre", "Grimpe à la corde par défaut, pour préserver votre jardin. Nacelle, grue ou autres machines quand la situation l'exige, et même hélicoptère quand aucun autre accès n'est possible."),
               ("Chantier rendu propre", "Branches broyées ou évacuées, terrain nettoyé. Vous ne vous occupez de rien.")],
              "Planifier une visite gratuite"),
    process_h2="Quatre étapes, du premier contact au terrain propre",
    process=[("Vous nous contactez", "Par le formulaire ou par téléphone. Quelques mots sur votre arbre suffisent pour démarrer."),
             ("Visite et diagnostic", "Nous venons voir l'arbre sur place, écoutons vos attentes et vous conseillons sur ce qu'il faut faire, ou ne pas faire."),
             ("Devis clair et gratuit", "Vous recevez un devis écrit et détaillé. Vous décidez en toute liberté."),
             ("Intervention et nettoyage", "Nous intervenons à la date convenue, sécurisons la zone et laissons votre jardin propre.")],
    gallery_h2="Nos interventions de taille",
    gallery=[("arboriste_grimpeur-3", "Arboriste-grimpeur au sommet d'un cèdre, lac de Neuchâtel en arrière-plan", "Taille en hauteur, Neuchâtel"),
             ("reduction_tilleul_porrentruy", "Tilleul après réduction de couronne à Porrentruy", "Réduction d'un tilleul, Porrentruy"),
             ("entretien_platanes_porrentruy", "Alignement de platanes entretenus à Porrentruy", "Entretien des platanes, Porrentruy"),
             ("degagement_facade_epicea", "Épicéa dégagé d'une façade par un arboriste-grimpeur", "Dégagement d'une façade"),
             ("arboriste_grimpeur-15", "Arboriste-grimpeur dans le feuillage", "Travail dans la couronne, à la corde"),
             ("plantation_arbre", "Jeune arbre planté avec tuteurage tripode à Neuchâtel", "Plantation et tuteurage tripode, Neuchâtel")],
    faq=[("Quelle est la bonne période pour tailler un arbre ?", "Cela dépend de l'essence et de l'objectif. La taille d'entretien se pratique souvent en hiver, hors gel, ou en été après la pousse. Certaines essences supportent mal la taille en période de montée de sève. Nous vous conseillons la période la plus favorable lors de la visite. <a href=\"/conseils/elagage-quand-et-pourquoi\">Lire notre article sur la période de taille</a>."),
         ("Combien coûte une taille d'arbre ?", "Le prix dépend de la taille de l'arbre, de son accessibilité, du type d'intervention et de l'évacuation des branches. C'est pourquoi nous nous déplaçons gratuitement pour établir un devis précis et écrit. Aucun engagement de votre part."),
         ("Faut-il une autorisation pour tailler ou abattre un arbre ?", "Une simple taille d'entretien ne nécessite en général aucune démarche. L'abattage, ou l'intervention sur un arbre protégé ou situé en zone particulière, peut être soumis à autorisation communale. Nous vous indiquons la marche à suivre selon votre commune."),
         ("Mon arbre est très grand ou difficile d'accès. Est-ce possible ?", "Oui. En tant qu'arboriste-grimpeur, nous accédons à la couronne à la corde, ce qui convient à la plupart des jardins, cours intérieures et terrains en pente. Quand c'est nécessaire, nous mobilisons une nacelle, une grue ou d'autres machines, et dans des cas très particuliers un hélicoptère."),
         ("Que deviennent les branches coupées ?", "Selon votre souhait et le devis, les branches sont broyées sur place, évacuées, ou le bois est laissé débité pour votre chauffage. Le terrain est nettoyé avant notre départ."),
         ("Pourquoi refusez-vous d'étêter un arbre ?", "L'étêtage crée de grosses plaies qui pourrissent, affaiblit l'arbre et provoque des rejets mal ancrés qui cassent facilement. Quelques années plus tard, l'arbre a repris sa hauteur et il est devenu dangereux. Nous proposons une réduction ciblée à la place.")],
    cta_img='entretien_platanes_porrentruy', cta_h2="Un doute sur un arbre ? Demandez l'avis d'un professionnel.", cta_lead="Visite et devis gratuits, sans engagement. Nous vous répondons sous 48 h ouvrées.",
)

ABATTAGE = dict(
    slug='abattage-demontage', nav="Abattage et démontage", nav_sub="Même près des bâtiments", icon='AXE', tag="",
    teaser="Abattage classique, démontage à la corde ou par rétention en zone contrainte, levage à la grue. Y compris près des bâtiments.",
    service_type="Abattage et démontage d'arbres",
    title="Abattage et démontage d'arbres – Arboriste | Arboritaille",
    desc="Abattage et démontage d'arbres par un arboriste-grimpeur, même près des bâtiments. Devis gratuit dans le Jura, à Neuchâtel, Bienne, Fribourg et Vaud.",
    hero_img='demontage_arbre_porrentruy', hero_pos='55% 35%', eyebrow="Abattage et démontage · Arboriste-grimpeur",
    h1="Abattage d'arbres <em>en toute sécurité</em>, même en espace restreint",
    lead="Arbre dangereux, mort, malade ou trop proche de la maison ? Un arboriste-grimpeur professionnel l'abat ou le démonte pièce par pièce, en préservant votre propriété, et laisse le terrain propre.",
    points=["Devis gratuit et sans engagement", "Intervention rapide en cas d'urgence", "Grimpe, nacelle, grue ou hélicoptère selon le cas", "Bois évacué, terrain nettoyé"],
    form_title="Devis abattage gratuit", form_sub="Décrivez l'arbre et son emplacement. Nous venons l'évaluer sur place, sans engagement.",
    form_options=["Abattage d'un arbre", "Démontage d'un arbre en zone contrainte", "Arbre dangereux / urgence après tempête", "Arbre mort ou malade", "Rognage de souche", "Plusieurs arbres à abattre", "Autre"],
    trust=[('SHIELD', "Arboriste-grimpeur", "Démontage à la corde, techniques de rétention"), ('WARN', "Urgences tempête", "Mise en sécurité rapide"), ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")],
    cards_eyebrow="Nos prestations d'abattage", cards_h2="La bonne technique pour chaque situation",
    cards_lead="Un arbre isolé dans un pré ne s'abat pas comme un sapin collé à une façade. Nous choisissons la méthode adaptée à votre terrain, vos bâtiments et vos voisins.",
    cards=[('AXE', "", "Abattage classique", "Quand l'espace le permet, l'arbre est abattu en une pièce, avec une direction de chute maîtrisée. Rapide et économique quand le terrain le permet."),
           ('SCISS', "Le plus courant", "Démontage par morceaux", "Le grimpeur monte dans l'arbre et le démonte branche par branche, puis tronçon par tronçon. Adapté en jardin, près d'une maison ou d'une ligne électrique."),
           ('LINK', "Zone contrainte", "Démontage par rétention", "Chaque pièce est attachée et descendue en douceur avec un système de freinage. Aucun morceau ne touche le sol sans contrôle : toitures, serres et massifs sont préservés."),
           ('CRANE', "", "Nacelle, grue et moyens spéciaux", "Quand la grimpe ne suffit pas, nous intervenons en nacelle ou faisons lever les sections à la grue. Dans les cas les plus rares, un hélicoptère peut être mobilisé. Nous organisons toute la logistique."),
           ('STUMP', "", "Rognage de souche", "Après l'abattage, la souche est rognée sous le niveau du sol. Vous pouvez replanter, semer du gazon ou reconstruire sans obstacle."),
           ('TREE', "", "Évacuation et valorisation du bois", "Branches broyées, bois de feu pour votre chauffage ou évacué. Le terrain est rendu propre, à vous de choisir.")],
    why=("Quand faut-il abattre un arbre", "Certains arbres doivent être abattus. Nous vous conseillons au cas par cas.",
         "Abattre n'est pas notre première option : si une taille ou un haubanage peut sauver l'arbre, nous vous le proposons. Mais dans certains cas, l'abattage est la seule option raisonnable.",
         [("Arbre dangereux", "Tronc fissuré, racines soulevées, penchant vers la maison ou la route : le risque de chute est réel, surtout par vent fort."),
          ("Arbre mort ou malade", "Champignons au pied, écorce qui se détache, houppier sec : un arbre dépérissant devient cassant et imprévisible."),
          ("Trop proche des bâtiments", "Racines qui soulèvent les dalles, branches sur la toiture, ombre permanente : l'arbre n'a plus sa place là où il a poussé."),
          ("Projet de construction", "Extension, piscine, nouvel accès : nous libérons l'emprise proprement, souche comprise, avant les travaux.")]),
    approach=("demontage_d-arbre_retention", "Démontage d'arbre par rétention, tronçon retenu par cordes", "Chaque pièce est retenue et contrôlée",
              "Notre méthode", "Un abattage propre, c'est d'abord un abattage préparé",
              "La sécurité de vos biens et des personnes dépend de la préparation. Chaque intervention est planifiée avant que la tronçonneuse ne démarre.",
              [("Visite et évaluation sur place", "Nous mesurons l'arbre, repérons les obstacles, les accès et les points d'ancrage, puis nous choisissons la technique et les moyens adaptés : grimpe, nacelle, grue ou, en dernier recours, hélicoptère."),
               ("Zone sécurisée pendant les travaux", "Périmètre balisé, protection des surfaces sensibles, coordination avec vous et vos voisins si nécessaire."),
               ("Descente contrôlée des pièces", "En démontage, rien ne tombe au hasard : chaque tronçon est guidé ou freiné jusqu'au sol."),
               ("Terrain rendu propre", "Bois évacué ou débité, branches broyées, sciure ramassée. Vous retrouvez votre jardin, sans la corvée.")],
              "Demander une évaluation gratuite"),
    process_h2="Quatre étapes, du premier appel au terrain propre",
    process=[("Vous nous contactez", "Décrivez l'arbre en quelques mots. En cas de danger immédiat, appelez-nous directement."),
             ("Visite et diagnostic", "Nous évaluons l'arbre et son environnement, et vous conseillons sur la méthode et sur une éventuelle autorisation communale."),
             ("Devis clair et gratuit", "Un devis écrit, avec ou sans rognage de souche et évacuation du bois."),
             ("Abattage et nettoyage", "Intervention à la date convenue, en sécurité. Le terrain est nettoyé avant notre départ.")],
    gallery_h2="Nos abattages et démontages",
    gallery=[("demontage_arbre_porrentruy", "Démontage d'un grand arbre à Porrentruy", "Démontage tronçon par tronçon, Porrentruy"),
             ("abattage_arbre_porrentruy-6", "Grue et camion lors d'un abattage", "Levage à la grue en zone urbaine"),
             ("abattage_sequoia", "Souche d'un séquoia abattu", "Abattage d'un séquoia"),
             ("abattage_arbre_porrentruy-3", "Tronc débité après abattage", "Bois débité, prêt à être évacué"),
             ("demontage_saule_bienne", "Arboriste-grimpeur démontant un saule à Bienne", "Démontage d'un saule, Bienne"),
             ("demontage_saule_port", "Démontage d'un saule avec cordes de rétention à Port", "Démontage d'un saule, Port")],
    faq=[("Faut-il une autorisation pour abattre un arbre ?", "Cela dépend du canton et de la commune. Dans le canton de Vaud, l'abattage d'un arbre protégé, en principe dès 40 cm de circonférence, et toute taille qui dépasse l'entretien courant demandent une autorisation de la commune. À Fribourg, Neuchâtel, dans le Jura et à Bienne, ce sont les règlements communaux qui désignent les arbres protégés. Nous vous indiquons la démarche et fournissons les éléments techniques nécessaires. <a href=\"/conseils/autorisation-abattage-arbre\">Le détail par canton</a>."),
         ("Combien coûte l'abattage d'un arbre ?", "Le prix dépend de la hauteur et du diamètre de l'arbre, de son accessibilité, de la technique nécessaire (abattage direct, démontage, rétention, grue) et de l'évacuation du bois. Un démontage en zone contrainte demande plus de temps qu'un abattage en plein champ. Nous établissons un devis précis et gratuit après visite."),
         ("Pouvez-vous abattre un arbre collé à ma maison ?", "Oui, c'est justement le cœur de notre métier. Par démontage à la corde et rétention, chaque pièce est descendue de manière contrôlée, sans toucher la toiture, la façade ou les aménagements."),
         ("Mon arbre est-il vraiment à abattre ?", "Pas forcément. Lors de la visite, nous examinons l'arbre avec attention. Si une taille de sécurité, un allègement ou un haubanage suffit à le conserver sans risque, nous vous le proposons en priorité."),
         ("Que faites-vous du bois et de la souche ?", "Selon le devis, le bois est débité en bûches pour votre chauffage, broyé ou évacué. La souche peut être laissée, coupée au ras du sol ou rognée pour permettre une replantation ou un engazonnement."),
         ("Intervenez-vous en urgence après une tempête ?", "Oui. Un arbre tombé sur un toit, une branche cassée qui menace de chuter ou un sujet déraciné : appelez-nous, nous intervenons au plus vite pour sécuriser les lieux. <a href=\"/urgence-tempete-arbre-dangereux\">Notre page urgence</a>.")],
    cta_img='abattage_arbre_porrentruy-6', cta_h2="Un arbre vous inquiète ? Faites-le évaluer gratuitement.", cta_lead="Visite et devis gratuits, sans engagement. En cas de danger immédiat, appelez-nous directement.",
)

SOUCHE = dict(
    slug='rognage-souche', nav="Rognage de souche", nav_sub="Replanter ou construire", icon='STUMP', tag="",
    teaser="Élimination des souches sous le niveau du sol pour replanter, engazonner ou construire sans obstacle.",
    service_type="Rognage et dessouchage",
    title="Rognage de souche et dessouchage – Arboriste | Arboritaille",
    desc="Souche rognée sous le niveau du sol pour replanter, semer ou construire. Machine compacte pour jardins étroits. Devis gratuit, Jura, Neuchâtel, Bienne, Fribourg, Vaud.",
    hero_img='abattage_sequoia', hero_pos='50% 55%', eyebrow="Rognage de souche · Arboriste-grimpeur",
    h1="Rognage de souche : <em>replantez ou construisez</em> sans obstacle",
    lead="Après un abattage, la souche gêne la tonte, la replantation ou un projet de construction. Nous la rognons sous le niveau du sol, avec une rogneuse adaptée à l'accès de votre terrain.",
    points=["Devis gratuit et sans engagement", "Rogneuse compacte pour les jardins étroits", "Copeaux laissés sur place ou évacués", "Replantation possible après rognage"],
    form_title="Devis rognage gratuit", form_sub="Indiquez le nombre de souches et leur diamètre approximatif. Nous passons voir l'accès.",
    form_options=["Rognage d'une souche", "Plusieurs souches", "Abattage puis rognage", "Souche ancienne avec rejets", "Souche avant construction ou terrassement", "Autre"],
    trust=[('STUMP', "Rognage sous le niveau du sol", "Profondeur adaptée à votre projet"), ('SHIELD', "Terrain préservé", "Machine compacte, passage par le portail"), ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")],
    cards_eyebrow="Nos prestations", cards_h2="Une solution pour chaque souche",
    cards_lead="Souche fraîche ou vieille de dix ans, isolée ou en alignement : la méthode dépend de son diamètre, de son essence et de ce que vous voulez faire du terrain.",
    cards=[('STUMP', "Le plus courant", "Rognage simple", "La souche est broyée sur 10 à 20 cm sous le niveau du sol. Suffisant pour semer du gazon ou poser une terrasse."),
           ('SPROUT', "", "Rognage profond avant replantation", "Rognage plus profond et évacuation des copeaux, puis apport de terre. L'emplacement est prêt pour un nouvel arbre."),
           ('TREE', "", "Souches multiples", "Haie abattue, alignement, verger renouvelé : nous enchaînons les souches en une intervention, avec un prix adapté au nombre."),
           ('WARN', "", "Souches qui rejettent", "Frêne, robinier, peuplier ou prunier repartent depuis la souche. Le rognage supprime la zone de rejets et met fin aux repousses."),
           ('CRANE', "", "Dessouchage mécanique", "Sur un chantier ou un terrain ouvert, la souche peut être arrachée à la pelle mécanique. Nous vous conseillons la méthode selon le terrain."),
           ('LEAF', "", "Remise en état", "Comblement avec de la terre végétale, nivellement et semis de gazon si vous le souhaitez. Le terrain redevient utilisable.")],
    why=("Pourquoi rogner une souche", "Une souche qui reste pose plusieurs problèmes dans la durée.",
         "Laisser une souche se décomposer prend des années. En attendant, elle gêne, repousse ou attire des champignons.",
         [("Entretien du jardin", "Tondre autour d'une souche abîme la tondeuse et laisse une zone d'herbes hautes. Une surface plane est plus simple à entretenir."),
          ("Replantation", "Pour replanter au même endroit, la souche et les grosses racines doivent être retirées et remplacées par de la terre."),
          ("Repousses", "Certaines essences rejettent vigoureusement depuis la souche pendant des années. Le rognage y met fin."),
          ("Champignons et sécurité", "Une souche en décomposition peut héberger l'armillaire, qui s'attaque aux arbres voisins. Elle reste aussi un obstacle où l'on trébuche.")]),
    approach=("abattage_arbre_porrentruy-3", "Tronc débité après abattage, prêt pour le rognage de la souche", "Rogneuse adaptée à l'accès",
              "Notre méthode", "Un rognage propre, sans surprise pour votre terrain",
              "Avant de démarrer la machine, nous vérifions ce qui se trouve autour et sous la souche.",
              [("Repérage des réseaux", "Canalisations, câbles, drainage, bordures : nous les localisons avec vous pour ne rien endommager."),
               ("Protection des surfaces", "Les copeaux sont projetés : nous protégeons façades, vitrages et massifs voisins."),
               ("Rognage à la profondeur utile", "Gazon, terrasse ou replantation : la profondeur dépend de votre projet, pas d'un réglage standard."),
               ("Copeaux et finition", "Copeaux laissés en paillage, étalés ou évacués. Comblement en terre sur demande.")],
              "Demander un devis gratuit"),
    process_h2="Quatre étapes, de la demande au terrain plat",
    process=[("Vous nous contactez", "Nombre de souches, diamètre approximatif, accès : quelques indications suffisent."),
             ("Visite ou photos", "Pour une souche simple, des photos suffisent souvent. Sinon, nous passons voir l'accès et les réseaux."),
             ("Devis clair et gratuit", "Avec ou sans évacuation des copeaux et remise en état."),
             ("Rognage et nettoyage", "Intervention à la date convenue. Le terrain est nivelé et nettoyé avant notre départ.")],
    gallery_h2="Après l'abattage",
    gallery=[("abattage_sequoia", "Souche d'un séquoia abattu avant rognage", "Souche de séquoia, avant rognage"),
             ("abattage_arbre_porrentruy-3", "Tronc débité après abattage", "Bois débité, souche à rogner"),
             ("abattage_arbre_porrentruy-6", "Grue lors d'un abattage en zone urbaine", "Abattage à la grue, Porrentruy")],
    faq=[("À quelle profondeur rognez-vous la souche ?", "En général 10 à 20 cm sous le niveau du sol, ce qui suffit pour du gazon ou une terrasse. Pour replanter un arbre au même endroit, nous rognons plus profond et retirons les grosses racines de surface."),
         ("Peut-on replanter au même endroit ?", "Oui, après un rognage profond et un apport de terre végétale. Si l'arbre abattu était malade, nous vous conseillons une autre essence ou un léger décalage."),
         ("Que deviennent les copeaux ?", "Les copeaux mélangés à la terre peuvent servir de paillage dans vos massifs, être étalés sur place ou évacués. Le choix figure dans le devis."),
         ("Pouvez-vous rogner une vieille souche ?", "Oui. Une souche ancienne, même partiellement décomposée ou couverte de rejets, se rogne sans difficulté particulière."),
         ("La rogneuse passe-t-elle dans mon jardin ?", "Nous disposons d'une rogneuse compacte qui passe par un portail de jardin standard. Pour les très grosses souches en terrain ouvert, une machine plus large ou une pelle mécanique peut être plus efficace."),
         ("Combien coûte un rognage de souche ?", "Le prix dépend du diamètre, du nombre de souches, de l'accès et de la finition souhaitée. Nous établissons un devis précis et gratuit, souvent sur photos.")],
    cta_img='abattage_arbre_porrentruy-3', cta_h2="Une souche vous encombre ? Faites-la disparaître.", cta_lead="Devis gratuit, souvent sur simple photo. Rognage propre, terrain remis à niveau.",
)

PLANTATION = dict(
    slug='plantation-arbres', nav="Plantation", nav_sub="La bonne essence au bon endroit", icon='SPROUT', tag="",
    teaser="Choix de l'essence adaptée au lieu, plantation dans les règles et tuteurage tripode pour une bonne reprise.",
    service_type="Plantation d'arbres",
    title="Plantation d'arbres par un arboriste | Arboritaille",
    desc="Arbres d'ornement et fruitiers : choix de l'essence selon le sol et le climat, plantation soignée, tuteurage tripode, compensation. Devis gratuit.",
    hero_img='plantation_arbre', hero_pos='50% 45%', eyebrow="Plantation · Arboriste-grimpeur",
    h1="Plantation d'arbres : <em>la bonne essence</em>, au bon endroit",
    lead="Un arbre bien choisi et bien planté demande peu d'interventions ensuite. Nous vous conseillons l'essence adaptée au sol, au climat et à l'espace disponible, puis nous plantons avec un tuteurage tripode.",
    points=["Conseil sur l'essence adaptée au lieu", "Tuteurage tripode, attaches souples", "Plantation de compensation après abattage", "Conseils d'arrosage pour les premières années"],
    form_title="Projet de plantation", form_sub="Décrivez le lieu et ce que vous attendez de l'arbre : ombre, fruits, écran, fleurs.",
    form_options=["Planter un arbre d'ornement", "Remplacer un arbre abattu (compensation)", "Planter un ou plusieurs fruitiers", "Alignement, verger ou plusieurs arbres", "Conseil sur le choix de l'essence", "Autre"],
    trust=[('SPROUT', "Essences adaptées", "Sol, climat, espace disponible"), ('LEAF', "Reprise favorisée", "Fosse large, tuteurage, arrosage"), ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")],
    cards_eyebrow="Nos prestations de plantation", cards_h2="De l'essence au premier été",
    cards_lead="Planter un arbre engage pour des décennies. Chaque étape compte, du choix de l'espèce au suivi des premières années.",
    cards=[('SEARCH', "", "Choix de l'essence", "Sol, exposition, place disponible à maturité, proximité des bâtiments et des limites : nous vous proposons des essences qui conviendront encore dans trente ans."),
           ('STUMP', "", "Préparation de la fosse", "Fosse large plutôt que profonde, sol décompacté, collet au niveau du terrain. Les erreurs de plantation se paient des années plus tard."),
           ('CABLE', "", "Tuteurage tripode", "Trois tuteurs et des attaches en caoutchouc maintiennent le tronc sans le blesser. L'arbre peut bouger légèrement et se renforcer."),
           ('LEAF', "Souvent exigée", "Plantation de compensation", "Une autorisation d'abattage est souvent assortie d'une obligation de replanter. Nous choisissons et plantons l'arbre de remplacement selon les exigences de la commune."),
           ('SPROUT', "", "Fruitiers et vergers haute-tige", "Pommiers, poiriers, cerisiers ou pruniers adaptés au climat : plantation, protection et taille de formation les premières années."),
           ('SCISS', "", "Taille de formation et suivi", "Guider la structure d'un jeune arbre évite les gros travaux plus tard. Nous proposons un suivi lors des premières années.")],
    why=("Pourquoi faire planter par un arboriste", "Un arbre qui réussit, c'est d'abord un arbre bien choisi.",
         "Beaucoup d'abattages que nous réalisons concernent des arbres plantés au mauvais endroit ou devenus trop grands. Un bon choix au départ évite ces situations.",
         [("Une essence adaptée au lieu", "Un arbre adapté au sol et au climat s'épanouit sans devenir problématique pour la maison, les voisins ou les réseaux."),
          ("Une plantation dans les règles", "Collet au bon niveau, racines dégagées, pas de tassement excessif : les gestes qui conditionnent la reprise."),
          ("Un départ sain", "La taille de formation des premières années donne une structure solide et limite les interventions futures."),
          ("Un climat qui change", "Les étés plus secs demandent des essences tolérantes. Nous tenons compte du climat de votre commune et de l'exposition du terrain.")]),
    approach=("plantation_arbre", "Jeune arbre planté avec tuteurage tripode à Neuchâtel", "Tuteurage tripode, attaches souples",
              "Notre méthode", "Planter pour trente ans, pas pour la photo",
              "Un jeune arbre bien installé est plus simple à conduire qu'un arbre adulte à corriger. Nous soignons chaque étape.",
              [("Visite et analyse du lieu", "Sol, humidité, exposition, réseaux enterrés, distances aux limites : nous observons avant de proposer."),
               ("Choix de l'essence et du calibre", "Nous vous présentons quelques essences adaptées, avec leur taille adulte et leurs besoins. Vous choisissez."),
               ("Plantation soignée", "Fosse large, collet au niveau du sol, arrosage abondant à la plantation et tuteurage tripode."),
               ("Arrosage et suivi", "Nous vous expliquons l'arrosage des deux premiers étés et pouvons revenir pour la taille de formation.")],
              "Demander un conseil gratuit"),
    process_h2="Quatre étapes, du projet au premier printemps",
    process=[("Vous nous contactez", "Dites-nous où vous voulez planter et ce que vous attendez de l'arbre."),
             ("Visite et conseil", "Nous analysons le lieu et vous proposons des essences adaptées, avec leur taille adulte."),
             ("Devis clair et gratuit", "Arbre, plantation, tuteurage et suivi : tout est détaillé."),
             ("Plantation", "À la bonne saison, en principe entre l'automne et le printemps, hors gel.")],
    gallery_h2="Jeunes arbres",
    gallery=[("plantation_arbre", "Jeune arbre planté avec tuteurage tripode à Neuchâtel", "Plantation et tuteurage tripode, Neuchâtel"),
             ("arboriste_grimpeur-15", "Arboriste-grimpeur dans le feuillage", "Suivi des arbres, à la corde"),
             ("entretien_platanes_porrentruy", "Alignement de platanes entretenus à Porrentruy", "Alignement conduit depuis la plantation, Porrentruy")],
    faq=[("Quand planter un arbre ?", "La période favorable va de l'automne au début du printemps, hors gel, quand l'arbre est au repos. Les arbres en conteneur peuvent se planter plus tard, à condition d'arroser régulièrement le premier été."),
         ("Quel arbre choisir dans le Jura ou sur le Plateau ?", "Cela dépend du sol, de l'altitude et de la place disponible. Érable champêtre, tilleul à petites feuilles, charme, chêne, cormier ou poirier sauvage supportent bien nos hivers et les étés plus secs. Nous vous proposons des essences adaptées lors de la visite."),
         ("À quelle distance de la maison et du voisin planter ?", "Les distances aux limites sont fixées par le droit cantonal et parfois par le règlement communal. Elles dépendent de la hauteur future de l'arbre. Nous vérifions les règles applicables à votre commune avant de planter."),
         ("Combien de temps faut-il arroser ?", "Les deux premiers étés sont décisifs : un arrosage abondant et espacé, plutôt qu'un peu tous les jours. Nous vous laissons des consignes simples adaptées à l'essence."),
         ("Peut-on replanter là où un arbre a été abattu ?", "Oui, après rognage de la souche et apport de terre. Si l'arbre précédent était malade, nous conseillons une autre essence."),
         ("Fournissez-vous les arbres ?", "Oui. Nous nous approvisionnons auprès de pépinières et choisissons des sujets bien formés, avec un système racinaire sain.")],
    cta_img='arboriste_grimpeur-15', cta_h2="Envie de planter un arbre qui durera ?", cta_lead="Conseil et devis gratuits. Nous vous aidons à choisir l'essence qui convient à votre terrain.",
)

HAUBANAGE = dict(
    slug='haubanage', nav="Haubanage", nav_sub="Consolider plutôt qu'abattre", icon='CABLE', tag="",
    teaser="Consolidation d'une fourche ou d'une charpentière fragile par haubanage dynamique ou statique, pour conserver l'arbre en sécurité.",
    service_type="Haubanage et consolidation d'arbres",
    title="Haubanage d'arbre – Consolidation | Arboritaille",
    desc="Haubanage dynamique ou statique pour consolider une fourche fendue ou une branche lourde et conserver l'arbre. Diagnostic et devis gratuits.",
    hero_img='arboriste_grimpeur-2', hero_pos='50% 30%', eyebrow="Haubanage · Arboriste-grimpeur",
    h1="Haubanage : <em>conserver un arbre fragilisé</em> plutôt que l'abattre",
    lead="Une fourche fendue, une charpentière lourde ou une écorce incluse ne condamnent pas forcément l'arbre. Un hauban posé au bon endroit de la couronne limite le risque de rupture et prolonge la vie de l'arbre.",
    points=["Diagnostic avant toute pose", "Haubans dynamiques ou statiques selon le défaut", "Contrôle périodique du système", "Une alternative sérieuse à l'abattage"],
    form_title="Avis sur un haubanage", form_sub="Décrivez le défaut que vous avez remarqué. Nous venons évaluer l'arbre sur place, sans engagement.",
    form_options=["Fourche fendue ou écorce incluse", "Branche lourde au-dessus d'une zone sensible", "Arbre ancien à conserver", "Contrôle d'un haubanage existant", "Je ne sais pas, j'ai besoin d'un avis", "Autre"],
    trust=[('CABLE', "Haubans dynamiques", "Sangles souples : l'arbre continue de se renforcer"), ('SHIELD', "Diagnostic mécanique", "Fourches, écorces incluses, fissures"), ('DOC', "Devis écrit et détaillé", "Gratuit, sans engagement")],
    cards_eyebrow="Nos prestations de haubanage", cards_h2="Le bon système pour le bon défaut",
    cards_lead="Un hauban ne se pose pas au hasard. Le type de système, sa hauteur et sa tension dépendent du défaut observé et de l'arbre.",
    cards=[('CABLE', "Le plus courant", "Haubanage dynamique", "Une sangle souple relie deux charpentières et absorbe les mouvements forts, par vent ou sous la neige. L'arbre continue de bouger et de se renforcer."),
           ('LINK', "", "Haubanage statique", "Quand une fissure est déjà ouverte, un système rigide empêche tout écartement supplémentaire. Souvent associé à une réduction de la branche."),
           ('LIFT', "", "Étayage", "Une branche basse très lourde, sur un arbre ancien, peut être soutenue par une béquille plutôt que supprimée."),
           ('SHRINK', "", "Allègement associé", "Réduire la longueur et le poids de la branche fragile diminue la contrainte sur le point faible. Hauban et allègement se complètent souvent."),
           ('CLOCK', "", "Contrôle et remplacement", "Les sangles ont une durée de vie limitée indiquée par le fabricant. Nous planifions un contrôle régulier et le remplacement quand il est nécessaire."),
           ('TREE', "", "Arbres remarquables", "Tilleul de village, chêne ancien, arbre protégé : le haubanage permet souvent de conserver un arbre que la commune ou le propriétaire tient à garder.")],
    why=("Quand envisager un haubanage", "Les défauts qui se consolident, plutôt que de condamner l'arbre",
         "Un haubanage se décide après observation. Voici les situations où il est souvent la bonne réponse.",
         [("Fourche à écorce incluse", "Deux axes qui poussent collés, avec de l'écorce coincée entre eux, forment un point faible. Un hauban répartit les efforts."),
          ("Fissure ou ancienne blessure", "Une fente visible, une ancienne cassure mal fermée : le hauban évite l'aggravation, souvent avec un allègement."),
          ("Branche lourde au-dessus d'une cible", "Toiture, terrasse, aire de jeux, place de parc : quand la branche ne peut pas être supprimée sans dénaturer l'arbre, on la sécurise."),
          ("Arbre que l'on veut garder", "Valeur patrimoniale, ombrage, attachement : quand l'abattage n'est pas souhaité, le haubanage offre une solution raisonnée.")]),
    approach=("arboriste_grimpeur-2", "Arboriste-grimpeur dans la couronne d'un grand arbre", "Posé en grimpe, dans la couronne",
              "Notre méthode", "Un haubanage utile commence par un diagnostic",
              "Poser un hauban sur un arbre qui n'en a pas besoin, ou au mauvais endroit, ne sert à rien. Nous observons d'abord.",
              [("Diagnostic du défaut", "Nature de la faiblesse, essence, vigueur, cible en dessous : nous évaluons le risque réel avant de proposer."),
               ("Choix du système", "Dynamique, statique ou étayage, avec la résistance adaptée au diamètre des axes à relier."),
               ("Pose en grimpe", "Nous installons le système au bon niveau de la couronne, sans percer ni blesser inutilement l'arbre."),
               ("Suivi dans le temps", "Nous notons la date de pose et vous proposons un contrôle régulier, car l'arbre grandit et les matériaux vieillissent.")],
              "Demander un diagnostic gratuit"),
    process_h2="Quatre étapes, du doute à l'arbre sécurisé",
    process=[("Vous nous contactez", "Décrivez ce que vous avez remarqué : fente, branche lourde, arbre qui vous inquiète."),
             ("Visite et diagnostic", "Nous examinons l'arbre et vous disons si un haubanage est pertinent, ou si une autre solution convient mieux."),
             ("Devis clair et gratuit", "Système, pose, éventuel allègement et contrôle futur : tout est détaillé."),
             ("Pose et consignes", "Installation en grimpe, puis quelques repères pour surveiller l'arbre entre deux contrôles.")],
    gallery_h2="Dans la couronne",
    gallery=[("arboriste_grimpeur-2", "Arboriste-grimpeur dans la couronne d'un grand arbre", "Travail dans la couronne"),
             ("arboriste_grimpeur-15", "Arboriste-grimpeur dans le feuillage", "Pose et contrôle à la corde"),
             ("reduction_tilleul_porrentruy", "Tilleul après réduction de couronne à Porrentruy", "Allègement d'un tilleul, Porrentruy")],
    faq=[("Haubanage dynamique ou statique : quelle différence ?", "Le dynamique utilise une sangle souple qui laisse l'arbre bouger et n'intervient que lors des mouvements forts. Le statique bloque l'écartement d'une fissure déjà ouverte. Le choix dépend du défaut observé."),
         ("Combien de temps dure un haubanage ?", "Les fabricants indiquent une durée de vie de leurs sangles, souvent de l'ordre de huit à douze ans. Nous conseillons un contrôle visuel régulier et un remplacement à l'échéance."),
         ("Le haubanage est-il visible ?", "Peu. Les sangles sont installées haut dans la couronne et se fondent dans le feuillage. En hiver, on les distingue en levant les yeux."),
         ("Peut-on hauban n'importe quel arbre ?", "Non. Si le bois est trop dégradé, si le défaut touche le tronc ou si la cible est trop sensible, l'abattage reste parfois la seule option raisonnable. Nous vous le dirons."),
         ("Combien coûte un haubanage ?", "Le prix dépend du nombre de systèmes, de la hauteur de pose et de l'éventuel allègement associé. Nous établissons un devis précis et gratuit après visite."),
         ("Le haubanage garantit-il qu'il n'y aura pas de casse ?", "Aucun système ne supprime tout risque. Le haubanage le réduit fortement, surtout combiné à un allègement et à un suivi régulier.")],
    cta_img='arboriste_grimpeur-3', cta_h2="Un arbre fragilisé que vous voulez garder ?", cta_lead="Diagnostic et devis gratuits. Nous vous disons si un haubanage peut le conserver en sécurité.",
)

DIAGNOSTIC = dict(
    slug='diagnostic-expertise-arbre', nav="Diagnostic et expertise", nav_sub="Conserver, soigner ou abattre", icon='SEARCH', tag="",
    teaser="Analyse de la vigueur, des défauts mécaniques et des pathologies. Un avis clair pour décider : conserver, soigner ou abattre.",
    service_type="Diagnostic et expertise d'arbres",
    title="Diagnostic et expertise d'arbre – Arboriste | Arboritaille",
    desc="Vigueur, défauts, champignons, risque de chute : un avis clair pour conserver, soigner ou abattre votre arbre. Rapport écrit sur demande.",
    hero_img='arboriste_grimpeur-3', hero_pos='50% 30%', eyebrow="Diagnostic et expertise · Arboriste-grimpeur",
    h1="Diagnostic d'arbre : <em>un avis clair</em> pour décider",
    lead="Un arbre penche, perd ses feuilles, montre des champignons au pied ? Nous analysons sa vigueur, ses défauts mécaniques et son environnement, puis nous vous disons ce qu'il faut faire : conserver, soigner, consolider ou abattre.",
    points=["Visite et premier avis gratuits", "Analyse des racines au houppier", "Rapport écrit sur demande", "Recommandations concrètes et chiffrées"],
    form_title="Demander un avis", form_sub="Décrivez ce qui vous inquiète. Une photo envoyée ensuite nous aide à préparer la visite.",
    form_options=["Un arbre m'inquiète (penché, fissuré, champignons)", "Avis avant achat ou vente d'un bien", "Expertise écrite pour la commune ou l'assurance", "Suivi d'un parc d'arbres", "Arbre proche d'un chantier", "Autre"],
    trust=[('SEARCH', "Lecture complète de l'arbre", "Racines, tronc, charpente, feuillage"), ('LEAF', "Vigueur et pathologies", "Champignons, dépérissement, chalarose"), ('DOC', "Rapport écrit sur demande", "Pour vos démarches")],
    cards_eyebrow="Nos prestations de diagnostic", cards_h2="Comprendre l'arbre avant de décider",
    cards_lead="Un diagnostic sérieux regarde l'arbre dans son ensemble et dans son contexte : ce qu'il montre, ce qu'il cache et ce qu'il menace.",
    cards=[('SEARCH', "La base", "Diagnostic visuel", "Observation méthodique du pied au houppier : collet, tronc, insertions des branches, bois mort, cavités, feuillage. La méthode de référence des arboristes."),
           ('LEAF', "", "Analyse de vigueur", "Longueur des pousses, densité du feuillage, cicatrisation des plaies : l'arbre nous dit s'il va bien ou s'il décline."),
           ('WARN', "", "Défauts mécaniques", "Fourches à écorce incluse, fissures, cavités, racines coupées ou soulevées : nous évaluons le risque de rupture et ce qu'il menace."),
           ('TREE', "", "Pathologies et champignons", "Chalarose du frêne, armillaire, polypores, chancres : nous identifions les signes et leurs conséquences pour la tenue de l'arbre."),
           ('DOC', "", "Expertise écrite", "Rapport avec photos, constats et recommandations, pour une demande d'abattage à la commune, une assurance ou une copropriété."),
           ('USERS', "", "Suivi de patrimoine arboré", "Pour les communes et les gérances : inventaire, priorités d'intervention et planification sur plusieurs années.")],
    why=("Quand demander un diagnostic", "Quatre situations où un avis évite une erreur",
         "Abattre un arbre sain ou garder un arbre dangereux : les deux erreurs coûtent cher. Un diagnostic permet de trancher sur des faits.",
         [("Signes d'alerte", "Champignons au pied, écorce qui se détache, branches sèches, tronc penché ou fissuré, feuillage clairsemé."),
          ("Avant des travaux", "Terrassement, construction ou tranchée près d'un arbre : les racines coupées fragilisent l'arbre pour des années. Nous évaluons avant."),
          ("Demande d'autorisation", "Beaucoup de communes demandent une justification pour abattre un arbre protégé. Un rapport d'arboriste appuie votre dossier."),
          ("Après une tempête", "Un arbre resté debout peut avoir bougé dans le sol ou s'être fissuré. Un contrôle évite une mauvaise surprise au prochain coup de vent.")]),
    approach=("arboriste_grimpeur-15", "Arboriste-grimpeur observant la couronne d'un arbre", "Un avis fondé sur l'observation",
              "Notre méthode", "Regarder, comprendre, puis recommander",
              "Nous ne venons pas avec une réponse toute faite. Chaque arbre est lu dans son contexte.",
              [("Historique et contexte", "Travaux récents, anciennes tailles, arrosage, changements autour de l'arbre : vous nous racontez, nous écoutons."),
               ("Observation du pied au houppier", "Collet et racines visibles, tronc, charpentières, bois mort, cavités, feuillage. Un contrôle en grimpe si nécessaire."),
               ("Évaluation du risque", "Probabilité de rupture et ce qui se trouve en dessous : une branche au-dessus d'un pré n'a pas le même enjeu qu'au-dessus d'une terrasse."),
               ("Recommandations", "Conserver, surveiller, alléger, hauban ou abattre : un avis clair, avec un devis si une intervention est utile.")],
              "Demander un avis gratuit"),
    process_h2="Quatre étapes, du doute à la décision",
    process=[("Vous nous contactez", "Décrivez ce qui vous inquiète. Des photos aident à préparer la visite."),
             ("Visite et observation", "Nous examinons l'arbre sur place et répondons à vos questions."),
             ("Avis et recommandations", "Un avis oral lors de la visite. Un rapport écrit si vous en avez besoin pour une démarche."),
             ("Intervention si nécessaire", "Si une taille, un haubanage ou un abattage s'impose, vous recevez un devis séparé.")],
    gallery_h2="Observer avant d'agir",
    gallery=[("arboriste_grimpeur-3", "Arboriste-grimpeur au sommet d'un cèdre, lac de Neuchâtel en arrière-plan", "Contrôle en hauteur, Neuchâtel"),
             ("arboriste_grimpeur-15", "Arboriste-grimpeur dans le feuillage", "Observation dans la couronne"),
             ("demontage_d-arbre_retention", "Démontage d'arbre par rétention", "Quand l'abattage s'impose : démontage par rétention")],
    faq=[("Le diagnostic est-il payant ?", "La visite et le premier avis oral sont gratuits, comme pour tout devis. Un rapport écrit détaillé, pour une commune, une assurance ou une copropriété, fait l'objet d'un devis."),
         ("Mon arbre penche : est-il dangereux ?", "Pas forcément. Beaucoup d'arbres penchent depuis toujours et sont bien ancrés. Ce qui compte, c'est un changement récent, un sol soulevé ou des fissures. Nous le vérifions sur place."),
         ("Un champignon au pied signifie-t-il qu'il faut abattre ?", "Non. Certains champignons sont sans gravité, d'autres dégradent le bois ou les racines. L'espèce, son emplacement et l'état de l'arbre déterminent la réponse."),
         ("Utilisez-vous des appareils de mesure ?", "Nous travaillons d'abord par observation méthodique, qui répond à la grande majorité des situations. Si un examen complémentaire est nécessaire, nous vous le disons et l'organisons."),
         ("Le rapport est-il accepté par la commune ?", "Nos rapports présentent des constats factuels, des photos et des recommandations. Les communes et les assurances s'appuient sur ce type de document pour instruire une demande."),
         ("Combien de temps dure un diagnostic ?", "Une visite dure en général entre trente minutes et une heure pour un arbre. Pour un parc ou un alignement, nous convenons d'un passage plus long.")],
    cta_img='arboriste_grimpeur-2', cta_h2="Un arbre vous pose question ?", cta_lead="Visite et premier avis gratuits. Nous vous disons ce que votre arbre a vraiment, et ce qu'il faut faire.",
)

URGENCE = dict(
    slug='urgence-tempete-arbre-dangereux', nav="Urgence tempête", nav_sub="Arbre tombé ou dangereux", icon='WARN', tag="Urgence",
    teaser="Branche cassée suspendue, arbre tombé sur un toit ou déraciné : nous sécurisons les lieux rapidement, puis nous évaluons l'arbre.",
    service_type="Mise en sécurité d'arbres dangereux et interventions après tempête",
    title="Arbre dangereux ou tombé : urgence tempête | Arboritaille",
    desc="Arbre tombé, branche suspendue, arbre déraciné après une tempête : mise en sécurité et démontage contrôlé. Appelez le 078 306 53 04.",
    hero_img='degagement_facade_epicea', hero_pos='50% 40%', eyebrow="Urgence · Arbre dangereux ou tombé",
    h1="Arbre dangereux ou tombé : <em>mise en sécurité</em> rapide",
    lead="Après un coup de vent, une branche cassée reste suspendue, un arbre penche vers la maison ou bloque un accès. Appelez-nous : nous sécurisons les lieux, puis nous évaluons calmement ce qu'il faut faire de l'arbre.",
    points=["Appel direct au 078 306 53 04", "Sécurisation en priorité, le reste ensuite", "Démontage contrôlé près des bâtiments", "Photos et facture détaillée pour votre assurance"],
    form_title="Signaler un arbre dangereux", form_sub="En cas de danger immédiat, appelez-nous. Sinon, décrivez la situation ici et nous vous rappelons rapidement.",
    form_options=["Arbre tombé sur un bâtiment ou un véhicule", "Branche cassée suspendue", "Arbre penché ou déraciné après tempête", "Arbre fissuré qui m'inquiète", "Dégagement d'un accès ou d'une route privée", "Autre"],
    trust=[('WARN', "Urgences tempête", "Sécurisation rapide"), ('SHIELD', "Démontage contrôlé", "Rétention, grue si nécessaire"), ('DOC', "Devis écrit", "Même en urgence, avant d'intervenir")],
    cards_eyebrow="Situations d'urgence", cards_h2="Ce que nous prenons en charge",
    cards_lead="Chaque situation demande une réponse adaptée : parfois une sécurisation provisoire suffit, parfois il faut démonter l'arbre le jour même.",
    cards=[('WARN', "Fréquent", "Branche cassée suspendue", "Une branche fendue retenue dans la couronne peut tomber à tout moment. Nous la descendons de manière contrôlée, à la corde."),
           ('HOME', "", "Arbre tombé sur un toit, une voiture, une clôture", "Démontage pièce par pièce, en évitant d'aggraver les dégâts. Les tronçons sont retenus et descendus sans choc."),
           ('WIND', "", "Arbre déraciné ou penché après tempête", "Sol soulevé, motte basculée : l'arbre peut finir de tomber. Nous le sécurisons puis le démontons ou l'abattons."),
           ('ARROW', "", "Dégagement d'accès", "Arbre couché sur un chemin, une entrée ou une place de parc : nous dégageons rapidement et évacuons le bois."),
           ('SHIELD', "", "Mise en sécurité provisoire", "Périmètre balisé, haubanage temporaire, suppression de la partie dangereuse : quand l'intervention complète doit attendre."),
           ('SEARCH', "", "Contrôle des autres arbres", "Une tempête révèle les faiblesses. Nous vérifions les arbres restés debout pour éviter la prochaine mauvaise surprise.")],
    why=("Pourquoi ne pas intervenir soi-même", "Un arbre tombé reste dangereux",
         "Les accidents graves surviennent souvent après la tempête, lors du nettoyage. Quelques raisons de nous appeler plutôt que de sortir la tronçonneuse.",
         [("Bois sous tension", "Un tronc couché ou une branche pliée stockent une énergie qui se libère à la coupe. Le bois peut fouetter ou rouler."),
          ("Chute de pièces", "Des branches cassées restent accrochées dans la couronne et tombent sans prévenir pendant le travail."),
          ("Toitures et lignes", "Travailler sur un toit ou près d'une ligne électrique demande un équipement et des techniques spécifiques."),
          ("Arbre encore enraciné", "Un arbre penché, partiellement déraciné, peut basculer quand on commence à le délester.")]),
    approach=("demontage_d-arbre_retention", "Démontage d'arbre par rétention, tronçon retenu par cordes", "Rien ne tombe sans contrôle",
              "Notre méthode", "Sécuriser d'abord, décider ensuite",
              "En urgence, l'ordre des opérations compte autant que la rapidité.",
              [("Premier échange au téléphone", "Vous décrivez la situation, si possible avec des photos. Nous vous disons quoi faire en attendant : éloigner les personnes, couper l'accès."),
               ("Sécurisation du périmètre", "Balisage, protection des zones sensibles, coordination avec les voisins ou la commune si la voie publique est touchée."),
               ("Démontage pièce par pièce", "Chaque tronçon est attaché et descendu avec un système de freinage. Grue si l'accès ou le poids l'exigent."),
               ("Nettoyage et conseil", "Bois évacué ou débité, terrain nettoyé. Nous vous conseillons sur l'arbre, la souche et une éventuelle replantation.")],
              "Appeler maintenant", f"tel:{PHONE_INTL}"),
    process_h2="Comment se déroule une intervention d'urgence",
    process=[("Vous nous appelez", "Décrivez la situation. En cas de danger pour des personnes, appelez d'abord les secours au 118 ou au 112."),
             ("Sécurisation", "Nous intervenons au plus vite pour supprimer le danger immédiat."),
             ("Devis pour la suite", "Démontage complet, rognage de souche, évacuation : un devis écrit, même en urgence."),
             ("Intervention et nettoyage", "Le terrain est rendu propre. Vous recevez les photos et la facture détaillée pour votre assurance.")],
    gallery_h2="Interventions en zone contrainte",
    gallery=[("degagement_facade_epicea", "Épicéa dégagé d'une façade par un arboriste-grimpeur", "Dégagement d'une façade"),
             ("demontage_d-arbre_retention", "Démontage d'arbre par rétention", "Démontage par rétention"),
             ("demontage_saule_port", "Démontage d'un saule avec cordes de rétention à Port", "Démontage d'un saule, Port"),
             ("abattage_arbre_porrentruy-6", "Grue et camion lors d'un abattage", "Levage à la grue, Porrentruy"),
             ("demontage_saule_bienne", "Arboriste-grimpeur démontant un saule à Bienne", "Démontage d'un saule, Bienne"),
             ("demontage_arbre_porrentruy", "Démontage d'un grand arbre à Porrentruy", "Démontage tronçon par tronçon, Porrentruy")],
    faq=[("En combien de temps pouvez-vous venir ?", "Appelez-nous : nous vous disons tout de suite quand nous pouvons être là. Les situations qui menacent des personnes ou des bâtiments passent en priorité."),
         ("Qui paie les dégâts causés par un arbre tombé ?", "Dans le Jura, à Neuchâtel, Berne, Fribourg et Vaud, l'établissement cantonal d'assurance des bâtiments (ECA Jura, ECAP, AIB, ECAB, ECA Vaud) couvre en principe les dommages de tempête aux bâtiments. Nous fournissons photos et facture détaillée pour votre dossier."),
         ("Faut-il une autorisation pour abattre un arbre dangereux ?", "En cas de danger immédiat, la sécurité prime : on sécurise d'abord. La plupart des règlements prévoient d'informer la commune, parfois avant, parfois juste après. Nous vous indiquons la démarche selon votre commune."),
         ("L'arbre peut-il être conservé après une tempête ?", "Parfois. Un arbre qui a perdu une branche peut être allégé et haubané. Un arbre dont le sol s'est soulevé est en général condamné. Nous vous donnons un avis honnête sur place."),
         ("Intervenez-vous le soir ou le week-end ?", "Appelez-nous dans tous les cas. Nous vous disons franchement si nous pouvons venir dans l'heure, le lendemain ou si une sécurisation provisoire est préférable."),
         ("Que faire en attendant votre arrivée ?", "Éloignez les personnes et les véhicules, ne passez pas sous la branche ou l'arbre, ne tentez pas de couper. Si une ligne électrique est touchée, prévenez le distributeur d'électricité.")],
    cta_img='abattage_arbre_porrentruy-6', cta_h2="Un arbre menace ou est tombé ?", cta_lead="Appelez-nous directement. Nous sécurisons les lieux, puis nous nous occupons du reste.",
)

SERVICES = [TAILLE, ABATTAGE, URGENCE, SOUCHE, HAUBANAGE, PLANTATION, DIAGNOSTIC]

# ---------------------------------------------------------------- Collectivités et entreprises
B2B = dict(
    title="Arbres des communes, gérances et entreprises | Arboritaille",
    desc="Pour communes, gérances et entreprises : suivi des arbres, arbres dangereux, abattage sur chantier, plantations. Un interlocuteur unique, des devis clairs.",
    hero_img='entretien_platanes_porrentruy', hero_pos='50% 50%', eyebrow="Collectivités · Gérances · Entreprises",
    h1="Entretien des arbres pour <em>collectivités, gérances et entreprises</em>",
    lead="Un parc d'arbres à suivre, un sujet dangereux à gérer, un arbre qui gêne un chantier : Arboritaille est votre partenaire pour l'entretien arboricole, avec un interlocuteur unique et des devis clairs.",
    points=["Un seul interlocuteur, du diagnostic au chantier", "Devis détaillés, planification sur l'année", "Interventions coordonnées avec vos services", "Rapports et photos pour vos dossiers"],
    form_title="Demande professionnelle", form_sub="Décrivez votre besoin : nombre d'arbres, site, échéance. Nous vous rappelons pour organiser une visite.",
    form_options=["Suivi du patrimoine arboré d'une commune", "Entretien des arbres d'immeubles (gérance, régie)", "Arbre à abattre ou à tailler sur un chantier", "Arbre dangereux sur un site", "Projet de plantation", "Expertise écrite", "Autre"],
    cards_eyebrow="Nos prestations", cards_h2="Ce que nous faisons pour les professionnels",
    cards_lead="Les mêmes techniques que pour les particuliers, avec la planification et les documents que vos services attendent.",
    cards=[('USERS', "Communes", "Suivi de groupes d'arbres", "Inventaire, contrôle régulier, priorités d'intervention et planification pluriannuelle pour les arbres d'alignement, de parcs et de cimetières."),
           ('WARN', "", "Gestion des sujets dangereux", "Évaluation du risque, mise en sécurité, allègement, haubanage ou abattage des arbres qui menacent la voie publique ou des bâtiments."),
           ('CRANE', "Entreprises", "Arbres sur chantier", "Un arbre nécessite des soins ou un abattage sur votre chantier ? Nous évaluons rapidement la situation et intervenons dès que possible, en coordination avec vos équipes."),
           ('HOME', "Gérances", "Patrimoine arboré d'immeubles", "Entretien régulier des arbres de vos immeubles et copropriétés, avec un interlocuteur unique, des devis clairs et un calendrier annuel."),
           ('SPROUT', "", "Projets de plantation", "Choix des essences, plantation, tuteurage et suivi des premières années, y compris les plantations de compensation exigées par les autorisations."),
           ('DOC', "", "Expertises et rapports", "Constats écrits avec photos et recommandations, pour les demandes d'autorisation, les assurances et les décisions de vos organes.")],
    approach=("entretien_platanes_porrentruy", "Alignement de platanes entretenus à Porrentruy", "Alignements, parcs, cimetières",
              "Notre façon de travailler", "Un partenaire qui connaît vos contraintes",
              "Procédures d'autorisation, sécurité du public, budget annuel, voisinage : nous intégrons vos contraintes dès le devis.",
              [("Visite et inventaire", "Nous parcourons le site avec vous, notons chaque arbre et ses enjeux, puis proposons des priorités."),
               ("Planification", "Interventions regroupées par saison et par secteur, pour limiter les déplacements et les coûts."),
               ("Sécurité et coordination", "Balisage, signalisation, information des riverains et coordination avec vos services techniques."),
               ("Documents", "Devis détaillés, photos avant et après, rapport d'intervention : ce qu'il faut pour vos dossiers et vos organes.")],
              "Organiser une visite"),
    process_h2="Comment démarrer",
    process=[("Vous nous contactez", "Décrivez le site et le besoin. Un plan ou une liste d'arbres aide, mais n'est pas indispensable."),
             ("Visite et inventaire", "Nous parcourons le site, évaluons chaque arbre et vous proposons des priorités."),
             ("Devis et planning", "Un devis détaillé, par intervention ou à l'année, avec un calendrier."),
             ("Interventions et rapport", "Travaux planifiés, site rendu propre, photos et rapport pour vos dossiers.")],
    faq=[("Travaillez-vous avec les petites communes ?", "Oui. Beaucoup de communes de notre zone ont quelques dizaines d'arbres à suivre, sans service des espaces verts. Nous proposons un passage annuel et des interventions groupées."),
         ("Pouvez-vous intervenir en urgence sur la voie publique ?", "Oui. Nous sécurisons la zone en coordination avec vos services et intervenons rapidement sur l'arbre."),
         ("Fournissez-vous des rapports écrits ?", "Oui. Constats, photos, recommandations et priorités, dans un format simple à transmettre à un conseil communal, une assemblée de copropriété ou une assurance."),
         ("Comment facturez-vous ?", "Par devis, à l'intervention ou sous forme de planning annuel chiffré. Les devis sont gratuits et détaillés."),
         ("Intervenez-vous près des lignes et des bâtiments ?", "Oui. Le démontage par rétention et le levage à la grue sont nos méthodes courantes en zone contrainte. Près des lignes électriques, nous coordonnons avec le distributeur."),
         ("Dans quelles communes intervenez-vous ?", "Dans le canton du Jura, à Neuchâtel, Bienne, Fribourg et dans le canton de Vaud. <a href=\"/zone-intervention\">Voir la zone d'intervention</a>.")],
    cta_h2="Un patrimoine arboré à gérer ?", cta_lead="Organisons une visite de votre site. Devis et planning détaillés, sans engagement.",
)

# ---------------------------------------------------------------- À propos
ABOUT = dict(
    title="À propos – Robin Humbert, arboriste-grimpeur à Courgenay | Arboritaille",
    desc="Arboritaille, c'est Robin Humbert, arboriste-grimpeur à Courgenay (JU) : taille, abattage, plantation et diagnostic, du Jura au canton de Vaud.",
    h1="Arboritaille, <em class=\"hl\">Robin Humbert</em>, arboriste-grimpeur",
    lead="La passion d'un métier, le respect du vivant, la sagesse des arbres.",
    img='arboriste_grimpeur-19', img_alt="Robin Humbert, arboriste-grimpeur, en intervention dans un arbre",
    body="""<h2>Une entreprise d'arboriste-grimpeur installée à Courgenay</h2>
<p>Arboritaille est l'entreprise individuelle de Robin Humbert, arboriste-grimpeur. Elle est inscrite au registre du commerce du canton du Jura depuis juin 2024, avec pour but la gestion du patrimoine arboré.</p>
<p>Depuis Courgenay, en Ajoie, nous intervenons dans le canton du Jura, à Neuchâtel, à Bienne et dans le canton de Berne, dans le canton de Fribourg et dans le canton de Vaud jusqu'à Lausanne et la Riviera.</p>
<h2>Le métier</h2>
<p>L'arboriste-grimpeur accède à la couronne de l'arbre à la corde, sans l'abîmer, pour tailler, démonter, hauban ou observer. Quand la grimpe ne suffit pas, nacelle, grue ou autres machines prennent le relais.</p>
<p>Notre travail commence toujours par une lecture de l'arbre : essence, vigueur, défauts, environnement. Puis nous choisissons l'intervention qui répond à votre besoin en respectant la physiologie de l'arbre.</p>
<h2>La taille raisonnée</h2>
<p>Un arbre ne cicatrise pas : il compartimente ses blessures. Chaque coupe a un effet durable. C'est pourquoi nous privilégions des coupes de petit diamètre, au bon endroit, et refusons l'étêtage.</p>
<p>Cette approche s'appuie sur les travaux de spécialistes de la biologie de l'arbre comme Christophe Drénou. <a href="/conseils/elagage-quand-et-pourquoi">Nous l'expliquons dans nos conseils</a>.</p>
<h2>Ce que disent nos clients</h2>
<p>Au 11 novembre 2026, notre fiche Google compte 12 avis, tous à 5 étoiles, en français et en allemand. Les clients citent le respect de la forme de l'arbre, la propreté du chantier et la rapidité du devis. <a href=\"""" + GBP_URL + """\" rel="noopener" target="_blank">Voir les avis sur Google</a>.</p>
<h2>Pour qui</h2>
<p>Particuliers, entreprises, gérances et collectivités : le même soin, adapté à vos enjeux. <a href="/collectivites-entreprises">Nos prestations pour les professionnels</a>.</p>
<p>Nous répondons par écrit en allemand et au téléphone en français.</p>""",
    values=("Nos engagements", "Quatre principes, sur chaque chantier",
            "Ce que vous pouvez attendre de nous, que l'arbre soit un tilleul de village ou un cerisier de jardin.",
            [("Conseiller avant de couper", "L'objectif est de conserver et d'embellir les arbres. Quand l'abattage s'impose, nous vous l'expliquons."),
             ("Respecter l'arbre", "Taille raisonnée, coupes propres, jamais d'étêtage. Des interventions qui durent."),
             ("Travailler en sécurité", "Grimpe à la corde, rétention, grue quand il faut : rien ne tombe sans contrôle."),
             ("Rendre un chantier propre", "Branches broyées ou évacuées, bois débité si vous le souhaitez, terrain nettoyé.")]),
)

CONTACT_BODY = """<h3>Horaires</h3>
<p>Du lundi au vendredi, de 8 h à 18 h. En dehors de ces horaires, laissez un message ou utilisez le formulaire : nous vous rappelons.</p>
<h3>Comment se passe une demande de devis</h3>
<p>Vous nous décrivez votre arbre. Nous convenons d'une visite sur place, gratuite, pour l'observer et écouter vos attentes. Vous recevez ensuite un devis écrit et détaillé, sans engagement.</p>
<h3>Urgence</h3>
<p>Arbre tombé, branche cassée suspendue, arbre penché après une tempête : appelez-nous directement. <a href="/urgence-tempete-arbre-dangereux">Notre page urgence</a> explique quoi faire en attendant.</p>
<h3>Langues</h3>
<p>Nous répondons en français par téléphone. Par e-mail et formulaire, nous répondons aussi en allemand.</p>"""

LEGAL = """<h2>Éditeur du site</h2>
<p>Arboritaille, Humbert Robin<br>Entreprise individuelle inscrite au registre du commerce du canton du Jura<br>Derrière-Metthiez 13, 2950 Courgenay, Suisse</p>
<p>IDE : CHE-424.403.827<br>N° RC : CH-670.1.009.977-2<br>N° TVA : CHE-424.403.827 TVA</p>
<p>Téléphone : <a href="tel:+41783065304">+41 78 306 53 04</a><br>E-mail : <a href="mailto:contact@arboritaille.ch">contact@arboritaille.ch</a></p>
<p>Responsable de la publication : Robin Humbert.</p>
<h2>Hébergement</h2>
<p>Hostinger International Ltd., 61 Lordou Vironos Street, 6023 Larnaca, Chypre.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, photographies et logos de ce site sont la propriété d'Arboritaille, sauf mention contraire. Toute reproduction sans autorisation écrite est interdite. Les photographies montrent des interventions réalisées par l'entreprise.</p>
<h2>Responsabilité</h2>
<p>Les informations de ce site, notamment celles qui concernent les règlements communaux et cantonaux sur les arbres, sont données à titre indicatif et peuvent évoluer. Elles ne remplacent pas un renseignement auprès de votre commune. Nous vérifions la procédure applicable lors de chaque devis.</p>
<h2>Données personnelles</h2>
<p>Voir notre page <a href="/protection-des-donnees">Protection des données</a>.</p>"""

PRIVACY = """<h2>Responsable du traitement</h2>
<p>Arboritaille, Humbert Robin, Derrière-Metthiez 13, 2950 Courgenay. Contact : <a href="mailto:contact@arboritaille.ch">contact@arboritaille.ch</a>.</p>
<p>Ce site est soumis à la loi fédérale suisse sur la protection des données (LPD). Lorsque le règlement général européen sur la protection des données (RGPD) s'applique, nous en respectons les exigences.</p>
<h2>Données que vous nous transmettez</h2>
<p>Lorsque vous remplissez un formulaire, nous recevons votre nom, votre téléphone, votre e-mail, votre localité, votre besoin et votre message, ainsi que la page utilisée et l'origine de votre visite (site, recherche Google, publicité).</p>
<p>Ces données servent uniquement à traiter votre demande : vous rappeler, organiser la visite, établir le devis. Elles sont transmises par e-mail à l'entreprise et enregistrées dans un outil de suivi des demandes (Google Workspace, via le service d'automatisation Make).</p>
<p>Elles ne sont ni vendues ni transmises à des tiers à des fins commerciales. Elles sont conservées le temps nécessaire au traitement de votre demande et à la relation commerciale, puis supprimées.</p>
<h2>Cookies et mesure d'audience</h2>
<p>Le site utilise Google Tag Manager pour mesurer les visites et l'efficacité de nos annonces Google (Google Ads, éventuellement Google Analytics). Ces outils ne sont activés que si vous cliquez sur « Tout accepter » dans le bandeau. Votre choix est conservé six mois dans votre navigateur.</p>
<p>Sans votre accord, aucun cookie publicitaire ou de mesure n'est déposé. Vous pouvez modifier votre choix à tout moment via le lien « Cookies » en bas de page.</p>
<p>Le site mémorise également dans votre navigateur, sans cookie et sans identification, l'origine de votre visite pendant 90 jours, uniquement pour indiquer dans le formulaire d'où provient votre demande.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par Hostinger International Ltd. Les journaux du serveur (adresse IP, pages consultées, date et heure) sont conservés par l'hébergeur pour des raisons de sécurité pendant une durée limitée.</p>
<h2>Vos droits</h2>
<p>Vous pouvez demander l'accès, la rectification ou la suppression de vos données, ou vous opposer à leur traitement, en écrivant à <a href="mailto:contact@arboritaille.ch">contact@arboritaille.ch</a>. Nous répondons dans un délai de 30 jours.</p>
<p>Dernière mise à jour : novembre 2026.</p>"""


def guides_teaser(GUIDES):
    """Bloc « Conseils » de l'accueil : trois guides."""
    keys = [k for k in ['elagage-quand-et-pourquoi', 'autorisation-abattage-arbre', 'arbre-dangereux-signes'] if k in GUIDES] or list(GUIDES)[:3]
    cards = ''.join(f'<a class="card card-link" href="/conseils/{k}"><span class="card-tag">{GUIDES[k].get("categorie", "Conseils")}</span><h3>{GUIDES[k]["titre_court"]}</h3><p>{GUIDES[k]["lead"][:150]}…</p></a>' for k in keys)
    return f'''<section class="section sand"><div class="wrap">
  <div class="center"><span class="eyebrow">Conseils d'arboriste</span><h2>Comprendre vos arbres avant de décider</h2><p class="lead">Période de taille, autorisations, arbres dangereux : nos réponses aux questions que nos clients nous posent.</p></div>
  <div class="services-grid">{cards}</div>
  <p class="center" style="margin-top:1.5rem"><a class="btn btn-outline" href="/conseils">Tous nos conseils</a></p>
</div></section>
'''
