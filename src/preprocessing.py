"""
Fonctions pour nettoyer et normaliser les saisies des prospects.
"""

import re

def clean_text(text):
    """
    Nettoie le texte saisi par l'utilisateur.
    
    Étapes :
    1. Vérifier que le texte n'est pas vide.
    2. Convertir en minuscules.
    3. Supprimer les caractères spéciaux (garder lettres, chiffres, espaces).
    4. Normaliser les espaces (supprimer les doubles, couper les extrémités).
    
    Args:
        text (str): Le texte brut saisi par l'utilisateur.
    
    Returns:
        str or None: Le texte nettoyé, ou None si le texte est vide.
    """
    # 1. Vérifier si le texte est vide ou composé uniquement d'espaces
    if text is None or not isinstance(text, str):
        return None
    if text.strip() == "":
        return None
    
    # 2. Convertir en minuscules
    text = text.lower()
    
    # 3. Supprimer les caractères spéciaux (garder lettres, chiffres, espaces)
    # (La ponctuation comme . , ! ? ; : est supprimée pour ne garder que les mots)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # 4. Normaliser les espaces : remplacer les espaces multiples par un seul
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text