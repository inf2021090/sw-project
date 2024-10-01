import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from utils.data_loader import load_data
from utils.info import display_info
from utils.algorithm_comparison import *
from ml.data_visualization import *
from ml.classification import *
from ml.clustering import *
from ml.feature_selection import *


def display_data(data):
    st.write("Data Table:")
    st.write(data)


def split_data(data):
    X = data.iloc[:, :-1]  # All columns except the last one are features
    y = data.iloc[:, -1]   # Last column is the target variable

    st.write("Features (X):")
    st.write(X)

    st.write("Labels (y):")
    st.write(y)

    return X, y


def main():
    st.title('Super Cool ML Application')

    # Option menu for navigation
    page = option_menu(
        menu_title="Navigation",
        options=["Upload Data", "Data Visualization", "Feature Selection", "Machine Learning", "Information"],
        icons=["upload", "bar-chart-line", "check-circle", "robot", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    # Page: Upload Data
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

            option = st.selectbox("Select Algorithm", ["None", "PCA Plot", "UMAP Plot"])

            if option == 'PCA Plot':
                if 'X' in st.session_state and 'y' in st.session_state:
                    pca_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")
            elif option == 'UMAP Plot':
                if 'X' in st.session_state and 'y' in st.session_state:
                    umap_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")

    if page == 'Machine Learning':
        st.title('Machine Learning')
        problem_type = 'Classification'

        if problem_type == 'Classification':
            st.write('Executing KNN and SVM for Classification...')

            if 'X' in st.session_state and 'y' in st.session_state:
                # KNN Classification
                k = st.slider("Select number of neighbors (k) for K-Nearest Neighbors", 1, 15, 3)
                
                # KNN on original data
                accuracy_knn, f1_knn, roc_auc_knn = knn(k, st.session_state.X, st.session_state.y)
                st.write(f"KNN Accuracy (Original): {accuracy_knn:.5f}")
                st.write(f"KNN F1 Score (Original): {f1_knn:.5f}")
                if roc_auc_knn is not None:
                    st.write(f"KNN ROC-AUC (Original): {roc_auc_knn:.5f}")

                # KNN on reduced data if available
                if 'X_selected' in st.session_state:
                    accuracy_knn_selected, f1_knn_selected, roc_auc_knn_selected = knn(k, st.session_state.X_selected, st.session_state.y)
                    st.write(f"KNN Accuracy (Reduced): {accuracy_knn_selected:.5f}")
                    st.write(f"KNN F1 Score (Reduced): {f1_knn_selected:.5f}")
                    if roc_auc_knn_selected is not None:
                        st.write(f"KNN ROC-AUC (Reduced): {roc_auc_knn_selected:.5f}")

                # SVM Classification
                kernel_option = st.selectbox("Select SVM Kernel", ["linear", "poly", "rbf"])
                C_value = st.slider("Select Regularization parameter (C) for SVM", 0.1, 10.0, 1.0)

                # SVM on original data
                accuracy_svm, f1_svm, roc_auc_svm = svm(st.session_state.X, st.session_state.y, kernel=kernel_option, C=C_value)
                st.write(f"SVM Accuracy (Original): {accuracy_svm:.5f}")
                st.write(f"SVM F1 Score (Original): {f1_svm:.5f}")
                if roc_auc_svm is not None:
                    st.write(f"SVM ROC-AUC (Original): {roc_auc_svm:.5f}")

                # SVM on reduced data if available
                if 'X_selected' in st.session_state:
                    # Check if X_selected has at least two features
                    if st.session_state.X_selected.shape[1] == 2:
                        accuracy_svm_selected, f1_svm_selected, roc_auc_svm_selected = svm(st.session_state.X_selected, st.session_state.y, kernel=kernel_option, C=C_value)
                        st.write(f"SVM Accuracy (Reduced): {accuracy_svm_selected:.5f}")
                        st.write(f"SVM F1 Score (Reduced): {f1_svm_selected:.5f}")
                        if roc_auc_svm is not None:
                            st.write(f"SVM ROC-AUC (Reduced): {roc_auc_svm_selected:.5f}")
                    else:
                        st.warning("Reduced dataset does not have 2 features for SVM visualization.")


            else:
                st.warning("Please upload data and split it before running Classification.")

    elif page == 'Feature Selection':
        st.title('Feature Selection')
        
        if 'X' in st.session_state and 'y' in st.session_state:
            k = st.slider("Select number of features to retain", 1, st.session_state.X.shape[1], 5)  # Update this line
            X_selected, selected_features = feature_selection(st.session_state.X, st.session_state.y, k)

            # Display the reduced dataset
            st.write("Reduced Dataset:")
            st.write(X_selected)

            # Store the reduced dataset in session state for later use
            st.session_state.X_selected = X_selected
            st.session_state.selected_features = selected_features

            st.success(f"Selected Features: {selected_features.tolist()}")

        else:
            st.warning("Please upload data and split it before running Feature Selection.")

    elif page == 'Information':
        display_info()


if __name__ == '__main__':
    main()
