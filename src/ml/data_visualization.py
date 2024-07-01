import streamlit as st
import numpy as np
import pandas as pd
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

def lda_plot(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    lda = LDA(n_components=2)
    X_lda = lda.fit_transform(X_scaled, y)

    plt.figure(figsize=(10, 8))
    for label in np.unique(y):
        plt.scatter(X_lda[y == label, 0], X_lda[y == label, 1], label=label)

    plt.title('LDA Plot')
    plt.xlabel('Linear Discriminant 1')
    plt.ylabel('Linear Discriminant 2')
    plt.legend()
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
