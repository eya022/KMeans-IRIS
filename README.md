# TP K-Means - Clustering Non Supervisé

## Description

Ce projet contient l'implémentation complète du TP sur l'algorithme K-Means appliqué au célèbre dataset Iris. Il s'agit d'un travail pratique de Data Mining réalisé dans le cadre du cours à la FST-Dep Info.

## Objectifs du TP

- Comprendre le fonctionnement de l'algorithme K-Means
- Appliquer le clustering sur des données réelles (Dataset Iris)
- Visualiser les résultats du partitionnement
- Évaluer la qualité du clustering
- Déterminer le nombre optimal de clusters

## Dataset

Le dataset **Iris** contient 150 observations de fleurs décrites par 4 variables :
- Longueur du sépale (cm)
- Largeur du sépale (cm)
- Longueur du pétale (cm)
- Largeur du pétale (cm)

3 espèces d'iris : Setosa, Versicolor, Virginica

## Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Bibliothèques nécessaires

```bash
pip install numpy pandas matplotlib scikit-learn
```

Ou utilisez le fichier requirements.txt :

```bash
pip install -r requirements.txt
```


## 💻 Utilisation

### Sur Windows

```bash
python tp_kmeans_windows.py
```

### Sur Linux/Mac

```bash
python tp_kmeans.py
```

Le script va :
1. Charger et explorer le dataset Iris
2. Appliquer l'algorithme K-Means avec 3 clusters
3. Générer des visualisations des clusters
4. Calculer l'inertie pour K=1 à 10 (Méthode du Coude)
5. Calculer le score de Silhouette pour K=2 à 10
6. Sauvegarder tous les résultats dans le dossier `resultats_kmeans/`

## 📈 Résultats

### Visualisations générées

1. **visualisation_clusters.png** : Graphiques 2D des clusters (Sépales et Pétales)
2. **elbow_method.png** : Courbe de l'inertie en fonction de K
3. **silhouette_method.png** : Score de Silhouette en fonction de K

### Métriques obtenues

- **Nombre optimal de clusters** : 3
- **Inertie pour K=3** : 78.86
- **Score de Silhouette pour K=3** : 0.5512
- **Distribution** : Cluster 0 (39), Cluster 1 (50), Cluster 2 (61)

## 🔍 Étapes du TP

### Étape 1 : Exploration des données
- Chargement du dataset Iris
- Affichage des dimensions et statistiques descriptives
- Conversion en DataFrame pandas

### Étape 2 : Application de K-Means
- Initialisation avec K=3 clusters
- Entraînement du modèle
- Prédiction des clusters

### Étape 3 : Visualisation
- Scatter plots des clusters
- Utilisation de couleurs pour différencier les groupes

### Étape 4 : Choix du nombre optimal de clusters
- **Méthode du Coude (Elbow Method)** : Analyse de l'inertie
- **Score de Silhouette** : Évaluation de la qualité du clustering

### Étape 5 : Interprétation
- Analyse des résultats
- Comparaison avec les vraies espèces
- Discussion des limites de K-Means

## 🛠️ Technologies utilisées

- **Python 3.13**
- **NumPy** : Calculs numériques
- **Pandas** : Manipulation de données
- **Matplotlib** : Visualisation
- **Scikit-learn** : Algorithme K-Means et métriques

##  Auteur

**Eya Jemai**  
  


## Licence

Ce projet est à usage éducatif dans le cadre du cours de Data Mining.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter des visualisations supplémentaires

## 📧 Contact

Pour toute question concernant ce TP, veuillez contacter votre enseignant ou ouvrir une issue sur GitHub.

---

**Note** : Ce TP fait partie du programme de Data Mining et illustre les concepts fondamentaux du clustering non supervisé.
