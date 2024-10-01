import streamlit as st
import numpy as np
import pandas as pd
import umap
from umap import UMAP

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import matplotlib.pyplot as plt
import seaborn as sns

def pca_plot(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=label)

    plt.title('PCA Plot')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    st.pyplot(plt)
    
def umap_plot(X, y):
    # Step 1: Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 2: Apply UMAP
    reducer = umap.UMAP(n_components=2, random_state=42)
    X_umap = reducer.fit_transform(X_scaled)

    # Step 3: Plot the UMAP-reduced data
    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_umap[y == label, 0], X_umap[y == label, 1], label=label)

    plt.title('UMAP Plot')
    plt.xlabel('UMAP 1')
    plt.ylabel('UMAP 2')
    plt.legend()
    
    # Step 4: Display the plot in Streamlit
    st.pyplot(plt)


def correlation_heatmap(data):
    numeric_data = data.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    st.pyplot(plt)

def pair_plot(data):
    plt.figure(figsize=(10, 8))
    sns.pairplot(data)
    st.pyplot(plt)

def box_plot(data):
    numeric_data = data.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.boxplot(data=numeric_data)
    plt.title('Box Plot')
    st.pyplot(plt)

def distribution_plot(data):
    for column in data.columns:
        plt.figure(figsize=(10, 4))
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        st.pyplot(plt)
