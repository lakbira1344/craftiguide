
SERVICE_DISPLAY = {
    "digital_strategy": "Stratégie digitale",
    "social_media": "Gestion des réseaux sociaux",
    "seo": "SEO & référencement naturel",
    "web_development": "Site vitrine & développement web",
    "ecommerce": "E-commerce",
    "web_application": "Application web sur mesure",
    "booking_system": "Système de réservation",
    "online_ads": "Publicité en ligne",
    "branding_identity": "Branding & identité visuelle",
    "content_marketing": "Content marketing",
    "print_production": "Print & production",
    "automation_ai": "Automatisation & solutions IA"
}


SECONDARY_SERVICES = {
    "digital_strategy": "SEO & référencement naturel",
    "social_media": "Content marketing",
    "seo": "Content marketing",
    "web_development": "SEO & référencement naturel",
    "ecommerce": "Publicité en ligne",
    "web_application": "Automatisation & solutions IA",
    "booking_system": "Site vitrine & développement web",
    "online_ads": "Stratégie digitale",
    "branding_identity": "Site vitrine & développement web",
    "content_marketing": "SEO & référencement naturel",
    "print_production": "Branding & identité visuelle",
    "automation_ai": "Application web sur mesure"
}


SERVICE_EXPLANATIONS = {
    "seo": "Votre demande semble liée à l'amélioration de la visibilité sur Google.",
    "ecommerce": "Votre demande concerne la vente de produits ou une boutique en ligne.",
    "web_development": "Votre demande concerne la création ou l'amélioration d'un site web professionnel.",
    "booking_system": "Votre demande semble liée à la gestion de réservations ou de rendez-vous.",
    "automation_ai": "Votre demande concerne l'automatisation ou l'intégration d'une solution intelligente.",
    "digital_strategy": "Votre demande concerne la définition d'une vision et d'un plan d'action digital.",
    "social_media": "Votre demande concerne la gestion et l'animation des réseaux sociaux.",
    "web_application": "Votre demande concerne le développement d'une application ou d'un outil métier.",
    "online_ads": "Votre demande concerne la publicité en ligne et l'acquisition de clients.",
    "branding_identity": "Votre demande concerne la création ou la refonte de l'identité visuelle de la marque.",
    "content_marketing": "Votre demande concerne la création de contenu pour attirer et informer les prospects.",
    "print_production": "Votre demande concerne la conception et l'impression de supports physiques."
}


def get_service_display(category):
    """Retourne le nom lisible du service."""
    return SERVICE_DISPLAY.get(category, "Service non identifié")

def get_secondary_service(category):
    """Retourne le service complémentaire suggéré."""
    return SECONDARY_SERVICES.get(category, "Analyse complémentaire recommandée")

def get_explanation(category):
    """Retourne une explication simple de la recommandation."""
    return SERVICE_EXPLANATIONS.get(
        category,
        "Cette recommandation est basée sur les éléments détectés dans votre demande."
    )

def generate_internal_summary(user_text, service_name, secondary_service):
    return f"""
--- Résumé interne Craftigital ---

**Besoin exprimé :**
{user_text}

**Service principal recommandé :**
{service_name}

**Service complémentaire suggéré :**
{secondary_service}

**Note :**
Cette recommandation est générée automatiquement par CraftiGuide (modèle ML).
"""

