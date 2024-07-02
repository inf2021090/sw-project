from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import adjusted_rand_score

import matplotlib.pyplot as plt

def kmeans(k, X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    # Normalization
    X_train_norm = preprocessing.normalize(X_train)
    X_test_norm = preprocessing.normalize(X_test)

    # KMeans
    kmeans = KMeans(n_clusters=k, random_state=0, n_init='auto')
    kmeans.fit(X_train_norm)
    
    # Predict the clusters for the test set
    y_pred = kmeans.predict(X_test_norm)

    # Calculate the adjusted Rand index
    ari = adjusted_rand_score(y_test, y_pred)

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(X_test_norm[:, 0], X_test_norm[:, 1], c=y_pred, cmap='viridis', marker='o', edgecolor='k', s=50, alpha=0.7)
    centroids = kmeans.cluster_centers_
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroids')
    ax.set_title(f'KMeans Clustering (k={k})\nAdjusted Rand Index: {ari:.2f}')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    fig.colorbar(scatter, ax=ax, label='Cluster Label')
    plt.legend()
    plt.grid(True)

    return fig, ari

def gmm(n_components, X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    # Normalization
    X_train_norm = preprocessing.normalize(X_train)
    X_test_norm = preprocessing.normalize(X_test)

    # Gaussian Mixture Model
    gmm = GaussianMixture(n_components=n_components, random_state=0)
    gmm.fit(X_train_norm)
    
    # Predict the clusters for the test set
    y_pred = gmm.predict(X_test_norm)

    # Calculate the adjusted Rand index
    ari = adjusted_rand_score(y_test, y_pred)

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(X_test_norm[:, 0], X_test_norm[:, 1], c=y_pred, cmap='viridis', marker='o', edgecolor='k', s=50, alpha=0.7)
    ax.set_title(f'GMM Clustering (n_components={n_components})\nAdjusted Rand Index: {ari:.2f}')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    fig.colorbar(scatter, ax=ax, label='Cluster Label')
    plt.grid(True)

    return fig, ari