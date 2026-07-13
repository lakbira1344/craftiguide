import joblib
import os


model_path = "models/craftguide_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError("Le modèle n'existe pas")

model = joblib.load(model_path)

def predict_service(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Le texte ne peut pas être vide.")
    return model.predict([cleaned])[0]

if __name__ == "__main__":
    test_phrases = [
        "Je veux vendre des chaussures en ligne.",
        "Comment améliorer mon référencement sur Google ?",
        "Nous avons besoin d'un tableau de bord pour suivre les ventes.",
        "Est-ce que vous pouvez créer un système de réservation pour mon hôtel ?",
        "Mon entreprise a besoin d'un nouveau logo.",
        "Je cherche à automatiser l'envoi des emails.",
        "Nous voulons lancer une campagne publicitaire sur Facebook.",
        "Je ne sais pas quelle stratégie adopter pour mon business.",
        "Nous avons besoin d'articles de blog chaque semaine.",
        "Pouvez-vous gérer notre page Instagram ?"
    ]
    
    print(" PRÉDICTIONS  ")
    for phrase in test_phrases:
        try:
            pred = predict_service(phrase)
            print(f" '{phrase}' ->  {pred}")
        except Exception as e:
            print(f" Erreur avec '{phrase}' : {e}")