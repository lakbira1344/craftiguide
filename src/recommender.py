from .preprocessing import clean_text

KEYWORDS = {
    "Site vitrine": [
        "présenter", "entreprise", "activité", "services", "vitrine", 
        "professionnel", "cabinet", "association", "artisan", "plomberie",
        "société", "présence en ligne", "montrer", "coordonnées", "horaires"
    ],
    "Site e-commerce": [
        "vendre", "produits", "boutique", "panier", "paiement", "commande",
        "livraison", "catalogue", "marchand", "commercialiser", "vente",
        "en ligne", "payer", "client", "stock", "cosmétiques", "accessoires"
    ],
    "Landing page": [
        "lancement", "capturer", "leads", "promouvoir", "offre", "inscription",
        "webinaire", "téléchargement", "conversion", "email", "prospect"
    ],
    "Application web": [
        "outil", "gestion", "digitaliser", "processus", "interne", "métier",
        "personnalisée", "plateforme", "back-office", "suivi", "ressources",
        "humaines", "contrats", "workflow", "stock"
    ],
    "Système de réservation": [
        "réservation", "rendez-vous", "planning", "disponibilités", "calendrier",
        "réserver", "table", "consultant", "patient", "cours", "hôtel", "salon"
    ],
    "UI/UX et identité visuelle": [
        "design", "identité visuelle", "charte graphique", "logo", "ergonomie",
        "interface", "expérience utilisateur", "refonte", "image de marque",
        "moderne", "couleurs"
    ],
    "SEO et visibilité": [
        "référencement", "SEO", "Google", "visibilité", "positionnement",
        "moteurs de recherche", "trafic", "audit", "netlinking", "page",
        "première page"
    ],
    "Marketing digital": [
        "publicité", "campagnes", "réseaux sociaux", "communication", "acquisition",
        "Google Ads", "Facebook", "Instagram", "emailing", "stratégie",
        "ciblées", "retargeting"
    ],
    "Automatisation": [
        "automatiser", "tâches répétitives", "connecter", "CRM", "workflow",
        "gagner du temps", "processus", "relance", "facturation", "synchronisation",
        "robots", "notifications"
    ],
    "Solution IA": [
        "intelligence artificielle", "chatbot", "assistant", "analyse", "automatisation",
        "reconnaissance", "prédiction", "génération", "lead", "données", "prédictive"
    ]
}

COMPLEMENTARY = {
    "Site vitrine": ["SEO", "UI/UX"],
    "Site e-commerce": ["SEO", "Identité visuelle", "Marketing digital"],
    "Landing page": ["Marketing digital", "UI/UX", "SEO"],
    "Application web": ["UI/UX", "Automatisation", "Solution IA"],
    "Système de réservation": ["UI/UX", "Site vitrine"],
    "UI/UX et identité visuelle": ["Site vitrine", "Marketing digital"],
    "SEO et visibilité": ["Marketing digital", "Site vitrine", "E-commerce"],
    "Marketing digital": ["SEO", "Landing page", "Identité visuelle"],
    "Automatisation": ["Application web", "Solution IA"],
    "Solution IA": ["Application web", "Automatisation", "Marketing digital"]
}

def recommend_service(user_text):
    cleaned_text = clean_text(user_text)
    
    if cleaned_text is None:
        return {
            "service": None,
            "score": 0,
            "reason": "Le texte est vide ou ne contient que des espaces. Veuillez reformuler votre demande.",
            "complementary_services": [],
            "ambiguous": True
        }

    words = cleaned_text.split()
    if len(words) < 3:
        return {
            "service": None,
            "score": 0,
            "reason": "Votre demande est trop courte. Pour une meilleure recommandation, décrivez votre besoin en quelques mots (ex: 'Je veux vendre mes produits en ligne').",
            "complementary_services": [],
            "ambiguous": True
        }
   
    scores = {}
    matched_words = {}
    
    for category, keywords in KEYWORDS.items():
        score = 0
        found = []
        for keyword in keywords:
            if keyword in cleaned_text:
                score += 1
                found.append(keyword)
        scores[category] = score
        matched_words[category] = found
    
    max_score = max(scores.values()) if scores else 0

    if max_score == 0:
        return {
            "service": None,
            "score": 0,
            "reason": "Je n'ai pas reconnu de mots-clés spécifiques dans votre demande. Pouvez-vous préciser votre besoin ? (ex: vente en ligne, site vitrine, référencement...)",
            "complementary_services": [],
            "ambiguous": True
        }

    best_categories = [cat for cat, sc in scores.items() if sc == max_score]

    if len(best_categories) > 1:
       
        return {
            "service": None,
            "score": max_score,
            "reason": f"Votre demande pourrait correspondre à plusieurs services : {', '.join(best_categories)}. Pouvez-vous préciser votre objectif principal ?",
            "complementary_services": [],
            "ambiguous": True
        }
    
    chosen_service = best_categories[0]
    
  
    found_words = matched_words[chosen_service]
    reason = f"La demande contient des termes liés à '{chosen_service}' : {', '.join(found_words[:5])}."
    
    complementary = COMPLEMENTARY.get(chosen_service, [])
 
    return {
        "service": chosen_service,
        "score": max_score,
        "reason": reason,
        "complementary_services": complementary,
        "ambiguous": False
    }