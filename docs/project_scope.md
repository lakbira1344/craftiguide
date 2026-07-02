# Project Scope - CraftiGuide

## 1. Problème traité et valeur attendue pour Craftigital

**Problème :**  
Les prospects de Craftigital expriment souvent leur besoin de manière générale, sans connaître le service le plus pertinent pour leur activité. L'équipe commerciale doit poser des questions supplémentaires pour identifier le bon service, ce qui allonge le cycle de vente.

**Valeur attendue :**  
CraftiGuide doit devenir un outil interne et commercial capable de structurer une demande, d’identifier l’objectif principal du prospect et de recommander les services Craftigital les plus adaptés.

## 2. Utilisateurs concernés

- **Prospect** : Personne ou entreprise qui exprime un besoin digital sans connaître précisément les services disponibles.
- **Équipe commerciale** : Utilisateur principal de l'outil. Il saisit la demande du prospect et utilise la recommandation pour orienter la proposition.
- **Chef de projet** : Valide la pertinence des services recommandés avant le lancement du projet.

## 3. Parcours de qualification d'un prospect

1. Le prospect décrit son besoin de manière générale.
2. L'équipe commerciale saisit la description dans CraftiGuide.
3. Le système structure la demande, identifie l'objectif principal.
4. Le moteur recommande les services les plus adaptés.
5. Le système retourne : service principal, justification, score, services complémentaires.
6. En cas de demande ambiguë ou insuffisante, un message clair est retourné.

## 4. Entrées, traitements et sorties du système

**Entrée :**  
Description courte du besoin d’un prospect (texte libre en français).

**Traitements :**  
- Nettoyage du texte (minuscules, suppression des caractères inutiles).  
- Comparaison avec un dictionnaire de mots-clés.  
- Calcul d’un score par catégorie de service.

**Sorties :**  
- Service principal recommandé.  
- Justification simple.  
- Score ou niveau de correspondance.  
- Services complémentaires pertinents.  
- Message clair pour les demandes ambiguës ou insuffisantes.

## 5. Limites de la première version

- Pas d'intelligence artificielle ni de Machine Learning (seulement des règles et mots-clés).
- Ne gère que les 10 catégories de services définies.
- Ne comprend pas le contexte complexe ou les négations.
- Pas de dialogue interactif avec le prospect.

## 6. Évolutions futures

- Introduction du Machine Learning après validation de cette fondation.
- Extension à d'autres catégories de services.
- Intégration dans un formulaire web ou une API.