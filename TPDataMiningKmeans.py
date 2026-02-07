# TP K-Means - Data Mining
# FST-Dep Info - Mohamed Lassoued
# Version Windows

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
import os

# Créer un dossier pour sauvegarder les résultats
output_dir = "resultats_kmeans"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("="*60)
print("ÉTAPE 1 : EXPLORATION ET COMPRÉHENSION DES DONNÉES")
print("="*60)

# Question 1 : Charger le dataset Iris
iris = load_iris()
X = iris.data 

# Question 2 : Afficher la taille et les premières lignes
print("\nTaille de X:", X.shape)
print("\nLes 5 premières lignes de X:")
print(X[:5])

# Question 3 : Créer un DataFrame pour une meilleure visualisation
df = pd.DataFrame(X, columns=['Longueur_Sepale', 'Largeur_Sepale', 'Longueur_Petale', 'Largeur_Petale'])

print("\nAffichage des 5 premières observations du DataFrame:")
print(df.head())

print("\nRésumé statistique des données:")
print(df.describe())

print("\n" + "="*60)
print("ÉTAPE 2 : APPLICATION DE L'ALGORITHME K-MEANS")
print("="*60)

# Appliquer K-means avec 3 clusters (car il y a 3 espèces)
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
kmeans.fit(X)

# Prédire les clusters
clusters = kmeans.predict(X)

print("\nClusters prédits pour toutes les observations:")
print(clusters)

# Ajouter les clusters au DataFrame
df['Cluster'] = clusters

print("\nDataFrame avec les clusters assignés:")
print(df.head(10))

print("\n" + "="*60)
print("ÉTAPE 3 : VISUALISATION DES CLUSTERS")
print("="*60)

# Visualisation 1 : Longueur vs Largeur des Sépales
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', s=50)
plt.xlabel('Longueur du Sépale (cm)')
plt.ylabel('Largeur du Sépale (cm)')
plt.title('Clustering K-Means - Sépales')
plt.colorbar(label='Cluster')

# Visualisation 2 : Longueur vs Largeur des Pétales
plt.subplot(1, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=clusters, cmap='viridis', s=50)
plt.xlabel('Longueur du Pétale (cm)')
plt.ylabel('Largeur du Pétale (cm)')
plt.title('Clustering K-Means - Pétales')
plt.colorbar(label='Cluster')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'visualisation_clusters.png'))
print(f"\nGraphique sauvegardé dans : {output_dir}/visualisation_clusters.png")
plt.show()

print("\n" + "="*60)
print("ÉTAPE 4 : CHOIX DU NOMBRE OPTIMAL DE CLUSTERS")
print("="*60)

# A. Méthode de l'inertie (Elbow Method)
print("\nA. Méthode de l'Inertie (Elbow Method)")

inerties = []
K_range = range(1, 11)

for k in K_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans_temp.fit(X)
    inerties.append(kmeans_temp.inertia_)

print("\nInertie pour chaque valeur de K:")
for k, inertia in zip(K_range, inerties):
    print(f"K = {k}: Inertie = {inertia:.2f}")

# Graphique de la méthode du coude
plt.figure(figsize=(10, 5))
plt.plot(K_range, inerties, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Nombre de clusters (K)')
plt.ylabel('Inertie')
plt.title('Méthode du Coude (Elbow Method)')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'elbow_method.png'))
print(f"\nGraphique sauvegardé dans : {output_dir}/elbow_method.png")
plt.show()

# B. Méthode du score de silhouette
print("\nB. Méthode du Score de Silhouette")

silhouette_scores = []
K_range_silhouette = range(2, 11)

for k in K_range_silhouette:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init='auto')
    labels = kmeans_temp.fit_predict(X)
    score = silhouette_score(X, labels)
    silhouette_scores.append(score)

print("\nScore de Silhouette pour chaque valeur de K:")
for k, score in zip(K_range_silhouette, silhouette_scores):
    print(f"K = {k}: Score de Silhouette = {score:.4f}")

# Graphique du score de silhouette
plt.figure(figsize=(10, 5))
plt.plot(K_range_silhouette, silhouette_scores, 'ro-', linewidth=2, markersize=8)
plt.xlabel('Nombre de clusters (K)')
plt.ylabel('Score de Silhouette')
plt.title('Méthode du Score de Silhouette')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'silhouette_method.png'))
print(f"\nGraphique sauvegardé dans : {output_dir}/silhouette_method.png")
plt.show()

print("\n" + "="*60)
print("ÉTAPE 5 : INTERPRÉTATION ET RÉSULTATS")
print("="*60)

print(f"\nNombre de clusters optimal suggéré : 3")
print(f"Inertie pour K=3 : {inerties[2]:.2f}")
print(f"Score de Silhouette pour K=3 : {silhouette_scores[1]:.4f}")

# Afficher les centres des clusters
print("\nCentres des clusters (centroïdes) pour K=3:")
print(kmeans.cluster_centers_)

# Compter le nombre d'observations par cluster
print("\nNombre d'observations par cluster:")
unique, counts = np.unique(clusters, return_counts=True)
for cluster_id, count in zip(unique, counts):
    print(f"Cluster {cluster_id}: {count} observations")

# Sauvegarder le DataFrame avec les clusters
df.to_csv(os.path.join(output_dir, 'iris_clusters.csv'), index=False)
print(f"\nDataFrame sauvegardé dans : {output_dir}/iris_clusters.csv")

print("\n" + "="*60)
print("FIN DU TP")
print("="*60)
print(f"\nTous les résultats ont été sauvegardés dans le dossier : {output_dir}/")