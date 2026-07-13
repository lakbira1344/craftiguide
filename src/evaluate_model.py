

import pandas as pd
import joblib
import os
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/craftiguide_dataset_training.csv")
X = df["text"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model_path = "models/craftguide_model.pkl"
if not os.path.exists(model_path):
    print(" Le modèle n'existe pas. Exécute d'abord train_model.py")
    exit()

model = joblib.load(model_path)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f" Accuracy du modèle : {accuracy:.2f}")

report = classification_report(y_test, y_pred, zero_division=0)
print("\n Rapport de classification :")
print(report)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(12, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Matrice de confusion - Meilleur modèle")
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.tight_layout()
plt.savefig("reports/confusion_matrix.png")
print(" Matrice sauvegardée dans reports/confusion_matrix.png")

from src.recommender import recommend_service

test_queries = [
    "Je veux vendre mes produits sur internet.",
    "Je souhaite mieux apparaître sur Google à Marrakech.",
    "Notre équipe veut remplacer ses fichiers Excel par une plateforme.",
    "Je veux que mes clients prennent rendez-vous en ligne.",
    "Nous avons besoin d'un logo et d'une charte graphique.",
    "Je cherche à automatiser les réponses aux prospects.",
    "Nous voulons lancer des publicités Facebook pour obtenir des ventes.",
    "Je ne sais pas quelle stratégie digitale suivre pour mon entreprise.",
    "Nous avons besoin d'articles pour notre blog.",
    "Je veux gérer régulièrement notre page Instagram.",
    "Je veux une boutique en ligne avec paiement sécurisé.",
    "J'ai besoin d'optimiser le référencement de mon site.",
    "Je souhaite un site vitrine moderne.",
    "Je veux un système de gestion des stocks.",
    "Nous cherchons une application pour gérer les clients.",
    "Je veux une landing page pour promouvoir une offre.",
    "Je cherche des cartes de visite.",
    "Je veux un chatbot pour mon site.",
    "Je souhaite une refonte de mon site actuel.",
    "Je veux gérer mes réservations en ligne."
]

results = []
for query in test_queries:
   
    kw_result = recommend_service(query)
    kw_pred = kw_result.get("service", "Non reconnu")
    
    ml_pred = model.predict([query])[0]
    
    results.append({
        "Texte": query,
        "Mots_Cles_Predit": kw_pred,
        "ML_Predit": ml_pred
    })

df_compare = pd.DataFrame(results)
df_compare.to_csv("reports/keyword_vs_ml.csv", index=False, encoding='utf-8')
print("Comparaison sauvegardée dans reports/keyword_vs_ml.csv")
print(df_compare.head(10))  