"""
Bloc E - Analyse et contrôle qualité des données
Script utilisant Pandas pour vérifier la qualité du dataset.
"""

import pandas as pd
import os

# ---- 1. Chargement du dataset ----
print("=" * 60)
print("ANALYSE DE LA QUALITÉ DU DATASET")
print("=" * 60)

# Charger le fichier CSV
file_path = "data/services_dataset.csv"
df = pd.read_csv(file_path)

print(f"\n✅ Fichier chargé : {file_path}")
print(f"   - Nombre de lignes : {len(df)}")
print(f"   - Nombre de colonnes : {len(df.columns)}")
print(f"   - Colonnes : {list(df.columns)}")

# ---- 2. Nombre total d'exemples et nombre de catégories ----
print("\n" + "-" * 60)
print("1. STATISTIQUES GÉNÉRALES")
print("-" * 60)

total_exemples = len(df)
nombre_categories = df['category'].nunique()

print(f"   - Nombre total d'exemples : {total_exemples}")
print(f"   - Nombre de catégories distinctes : {nombre_categories}")

# ---- 3. Répartition des exemples par catégorie ----
print("\n" + "-" * 60)
print("2. RÉPARTITION PAR CATÉGORIE")
print("-" * 60)

repartition = df['category'].value_counts()
print(repartition)

# ---- 4. Détection des valeurs manquantes ----
print("\n" + "-" * 60)
print("3. VALEURS MANQUANTES")
print("-" * 60)

valeurs_manquantes = df.isnull().sum()
if valeurs_manquantes.sum() == 0:
    print("   ✅ Aucune valeur manquante détectée.")
else:
    print("   ⚠️ Valeurs manquantes détectées :")
    print(valeurs_manquantes[valeurs_manquantes > 0])

# ---- 5. Détection des doublons ----
print("\n" + "-" * 60)
print("4. DOUBLONS")
print("-" * 60)

doublons = df.duplicated(subset=['text']).sum()
if doublons == 0:
    print("   ✅ Aucun doublon détecté.")
else:
    print(f"   ⚠️ {doublons} doublons détectés.")

# ---- 6. Identification des catégories sous-représentées ----
print("\n" + "-" * 60)
print("5. CATÉGORIES SOUS-REPRÉSENTÉES")
print("-" * 60)

seuil_min = 8
sous_representees = repartition[repartition < seuil_min]

if len(sous_representees) == 0:
    print(f"   ✅ Toutes les catégories ont au moins {seuil_min} exemples.")
else:
    print(f"   ⚠️ Catégories avec moins de {seuil_min} exemples :")
    print(sous_representees)

# ---- 7. Export du rapport ----
print("\n" + "-" * 60)
print("6. EXPORT DU RAPPORT")
print("-" * 60)

rapport_path = "docs/data_quality_report.md"

with open(rapport_path, "w", encoding="utf-8") as f:
    f.write("# Rapport de qualité des données - CraftiGuide\n\n")
    f.write(f"**Date de génération** : {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("## 1. Statistiques générales\n\n")
    f.write(f"- **Nombre total d'exemples** : {total_exemples}\n")
    f.write(f"- **Nombre de catégories distinctes** : {nombre_categories}\n\n")
    
    f.write("## 2. Répartition par catégorie\n\n")
    f.write("| Catégorie | Nombre d'exemples |\n")
    f.write("|-----------|-------------------|\n")
    for cat, count in repartition.items():
        f.write(f"| {cat} | {count} |\n")
    f.write("\n")
    
    f.write("## 3. Valeurs manquantes\n\n")
    if valeurs_manquantes.sum() == 0:
        f.write("✅ Aucune valeur manquante détectée.\n\n")
    else:
        f.write("⚠️ Valeurs manquantes détectées :\n\n")
        for col, count in valeurs_manquantes[valeurs_manquantes > 0].items():
            f.write(f"- **{col}** : {count} valeurs manquantes\n")
        f.write("\n")
    
    f.write("## 4. Doublons\n\n")
    if doublons == 0:
        f.write("✅ Aucun doublon détecté.\n\n")
    else:
        f.write(f"⚠️ {doublons} doublons détectés.\n\n")
    
    f.write("## 5. Catégories sous-représentées\n\n")
    f.write(f"**Seuil minimum requis** : {seuil_min} exemples par catégorie\n\n")
    if len(sous_representees) == 0:
        f.write("✅ Toutes les catégories respectent le seuil minimum.\n\n")
    else:
        f.write("⚠️ Catégories sous-représentées :\n\n")
        for cat, count in sous_representees.items():
            f.write(f"- **{cat}** : {count} exemples (manque {seuil_min - count})\n")
        f.write("\n")
    
    f.write("## 6. Conclusion\n\n")
    if (valeurs_manquantes.sum() == 0 and doublons == 0 and len(sous_representees) == 0):
        f.write("✅ Le dataset est de bonne qualité. Il peut être utilisé pour la suite du projet.\n")
    else:
        f.write("⚠️ Le dataset présente des anomalies. Une correction est recommandée avant la suite.\n")

print(f"   ✅ Rapport exporté dans : {rapport_path}")

# ---- 8. Résumé final ----
print("\n" + "=" * 60)
print("RÉSUMÉ DE L'ANALYSE")
print("=" * 60)

if (valeurs_manquantes.sum() == 0 and doublons == 0 and len(sous_representees) == 0):
    print("✅ QUALITÉ : BONNE - Le dataset est prêt pour la suite.")
else:
    print("⚠️ QUALITÉ : DES ANOMALIES DÉTECTÉES - Vérifiez le rapport.")
    
print("\n" + "=" * 60)
print("FIN DE L'ANALYSE")
print("=" * 60)