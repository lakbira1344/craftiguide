import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/craftiguide_dataset_training.csv")
X = df["text"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print("Taille train :", len(X_train))
print("Taille test :", len(X_test))
print("\n ENTRAÎNEMENT LOGISTIC REGRESSION ")
logistic_model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

logistic_model.fit(X_train, y_train)
y_pred = logistic_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print(report)
os.makedirs("reports", exist_ok=True)
with open("reports/classification_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

plt.figure(figsize=(12, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=logistic_model.classes_, yticklabels=logistic_model.classes_)
plt.title("Matrice de confusion - Logistic Regression")
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.tight_layout()
plt.savefig("reports/confusion_matrix.png")
print("\n ENTRAÎNEMENT NAIVE BAYES ")
nb_model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
    ("classifier", MultinomialNB())
])

nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)
accuracy_nb = accuracy_score(y_test, nb_pred)

print(f"Accuracy NB : {accuracy_nb:.2f}")
if accuracy >= accuracy_nb:
    best_model = logistic_model
    best_name = "LogisticRegression"
else:
    best_model = nb_model
    best_name = "NaiveBayes"

print(f"\n Meilleur modèle : {best_name} avec {max(accuracy, accuracy_nb):.2f} d'accuracy")

os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/craftguide_model.pkl")
print(" Modèle sauvegardé dans models/craftguide_model.pkl")

import csv
with open("reports/comparison_results.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Model", "Accuracy"])
    writer.writerow(["LogisticRegression", accuracy])
    writer.writerow(["MultinomialNB", accuracy_nb])
    writer.writerow(["Best_Model", best_name])

print(" Rapport de comparaison sauvegardé dans reports/comparison_results.csv") 