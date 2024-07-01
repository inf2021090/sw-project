import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.info import display_info
from ml.data_visualization import *
from ml.clustering import *


def display_data(data):
    st.write("Data Table:")
    st.write(data)

def split_data(data):
    X = data.iloc[:, :-1]  # All columns except the last one are features
    y = data.iloc[:, -1]   # Last column is the label

    st.write("Features (X):")
    st.write(X)

    st.write("Label (y):")
    st.write(y)

    return X, y

def main():
    st.title('Super Cool ML Application')

    # Sidebar navigation
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Upload Data', 'Information', 'Data Visualization', 'Machine Learning'))

    if page == 'Upload Data':
        st.title('Data Upload and Display')

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "xlsx"])

        if uploaded_file is None:
            st.warning('Please upload a file.')
            return

        try:
            data = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Error: {e}")
            return

        if data is None:
            st.error("Failed to load data. Please check your file.")
            return

        # Store data in session state
        st.session_state.data = data

        # Display uploaded data
        display_data(data)

        # Split dataset and assign X, y
        X, y = split_data(data)

        # Store X, y in session state
        st.session_state.X = X
        st.session_state.y = y

    elif page == 'Data Visualization':
        if 'data' not in st.session_state:
            st.warning("Please upload a file first in the 'Upload Data' section.")
        else:
            st.title("2D Visualization")

            # Choose a visualization type
            option = st.selectbox("Select Algorithm", ["None", "PCA Plot", "LDA Plot"])

            if option == 'PCA Plot':
                if 'X' in st.session_state and 'y' in st.session_state:
                    pca_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")

            elif option == 'LDA Plot':
                if 'X' in st.session_state and 'y' in st.session_state:
                    lda_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")

    elif page == 'Machine Learning':
        st.title('Machine Learning')
        st.write('Select problem(s): ')

        classification_selected = st.checkbox('Classification')
        clustering_selected = st.checkbox('Clustering')

        if classification_selected:
            classification_algorithm = st.selectbox('Select Classification Algorithm', ["None", "KNN", "Random Forests"])

        if clustering_selected:
            clustering_algorithm = st.selectbox('Select Clustering Algorithm', ["None", "K-Means", "GMM"])
            if clustering_algorithm == 'K-Means':
                k = st.slider("Select number of neighbors (k) for K-Nearest Neighbors", 1, 15, 3)
                st.write('K is:', k)
                if 'X' in st.session_state and 'y' in st.session_state:
                    fig, accuracy = knn(k, st.session_state.X, st.session_state.y)
                    st.pyplot(fig)
                    st.write(f"Accuracy: {accuracy:.2f}")
                else:
                    st.warning("Please upload data and split it before running KNN.")

        if not classification_selected and not clustering_selected:
            st.warning("Please select at least one problem type.")

    elif page == 'Information':
        display_info()

if __name__ == '__main__':
    main()
