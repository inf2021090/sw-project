import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import matplotlib.pyplot as plt

def pca_plot(X,y):
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Create scatter plot 
    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=label)

    plt.title('PCA Plot')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    st.pyplot(plt)

    # Optionally, return the PCA components for further analysis or visualization
    #return pca.components_

def lda_plot(X, y):
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform LDA
    lda = LDA(n_components=2)
    X_lda = lda.fit_transform(X_scaled, y)

    # Create scatter plot 
    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_lda[y == label, 0], X_lda[y == label, 1], label=label)

    plt.title('LDA Plot')
    plt.xlabel('Linear Discriminant 1')
    plt.ylabel('Linear Discriminant 2')
    plt.legend()
    st.pyplot(plt)

    # Optionally, return the LDA components for further analysis or visualization
    # return lda.coef_
