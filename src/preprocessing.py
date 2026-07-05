import re

def clean_text(text):
   
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