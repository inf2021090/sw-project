import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.info import display_info
from utils.algorithm_comparison import *
from ml.data_visualization import *
from ml.classification import *
from ml.clustering import *


def display_data(data):
    st.write("Data Table:")
    st.write(data)

def split_data(data):
    X = data.iloc[:, :-1]  # All columns except the last one are features
    y = data.iloc[:, -1]   # Last column is the target variable

    st.write("Features (X):")
    st.write(X)

    st.write("Target variable (y):")
    st.write(y)

    return X, y

def main():
    st.title('Super Cool ML Application')

    # Sidebar navigation
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Upload Data', 'Data Visualization', 'Machine Learning', 'Information'))

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

        # Choose a Machine Learning Problem
        problem_type = st.radio('Select Problem Type', ('Classification', 'Clustering'))

        if problem_type == 'Classification':
            st.write('Executing both Random Forests and Decision Trees for Classification...')

            if 'X' in st.session_state and 'y' in st.session_state:
                # Execute KNN
                k = st.slider("Select number of neighbors (k) for K-Nearest Neighbors", 1, 15, 3)
                fig_knn, accuracy_knn = knn(k, st.session_state.X, st.session_state.y)
                st.pyplot(fig_knn)
                st.write(f"KNN Accuracy: {accuracy_knn:.5f}")

                # Execute Decision Trees
                max_depth = st.slider("Select max depth of the tree for Decision Tree", 1, 15, 3)
                accuracy_dt, fig_dt_buf = decision_tree(st.session_state.X, st.session_state.y, max_depth)
                st.image(fig_dt_buf, caption='Decision Tree Visualization', use_column_width=True)
                st.write(f"Decision Trees Accuracy: {accuracy_dt:.5f}")

                # Make comparison
                result = compare_classifiers(accuracy_knn,accuracy_dt)
                st.write(result)

            else:
                st.warning("Please upload data and split it before running Classification.")

        if problem_type == 'Clustering':
            st.write('Executing both K-Means and Gaussian Mixture Model (GMM) for Clustering...')

            if 'X' in st.session_state and 'y' in st.session_state:
                # Execute K-Means
                k = st.slider("Select number of clusters (k) for K-Means", 5, 15, 3)
                st.write('K is:', k)
                fig_km, ari_km = kmeans(k, st.session_state.X, st.session_state.y)  
                st.pyplot(fig_km)
                st.write(f"K-Means Adjusted Rand Index: {ari_km:.5f}")

                # Execute GMM
                n_components = st.slider("Select number of components for GMM", 1, 15, 3)
                st.write('Number of components:', n_components)
                fig_gmm, ari_gmm = gmm(n_components, st.session_state.X, st.session_state.y)  
                st.pyplot(fig_gmm)
                st.write(f"GMM Adjusted Rand Index: {ari_gmm:.5f}")

                # Make comparison
                result = compare_clusters(ari_km, ari_gmm)
                st.write(result)

            else:
                st.warning("Please upload data before running Clustering.")

    elif page == 'Information':
        display_info()

if __name__ == '__main__':
    main()
