import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def pca_plot(data):
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1]   # Labels

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Create a scatter plot of the PCA results
    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=label)

    plt.title('PCA Plot')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    st.pyplot(plt)

    # Optionally, return the PCA components for further analysis or visualization
    return pca.components_
