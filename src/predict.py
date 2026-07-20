

import joblib

def load_model(model_path="models/craftguide_model.pkl"):
    """
    Charge le modèle sauvegardé depuis le dossier models/.
    """
    return joblib.load(model_path)

def predict_category(model, text):
    """
    Prend une phrase en entrée et retourne la catégorie prédite.
    """
    if not text or text.strip() == "":
        raise ValueError("Le texte ne peut pas être vide.")
    prediction = model.predict([text])
    return prediction[0]