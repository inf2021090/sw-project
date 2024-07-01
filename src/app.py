import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.info import display_info
from ml.data_visualization import *


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
    page = st.sidebar.radio("Go to", ('Upload Data', 'Information', 'Data Visualization'))

    if page == 'Upload Data':
        st.title('Data Upload and Display')

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "xlsx"])

        if uploaded_file is None:
            st.warning('Please upload a file.')
            return

        try:
            data = load_data(uploaded_file)
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
            st.header("2D Visualization")

            # Choose a visualization type
            option = st.selectbox("Select Algorithm", ["None", "PCA Plot", "LDA Plot"])

            if (option == 'PCA Plot'):
                if 'X' in st.session_state and 'y' in st.session_state:
                    pca_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")

            elif (option == 'LDA Plot'):
                if 'X' in st.session_state and 'y' in st.session_state:
                    lda_plot(st.session_state.X, st.session_state.y)
                    correlation_heatmap(st.session_state.data)
                    box_plot(st.session_state.data)
                    distribution_plot(st.session_state.data)
                else:
                    st.warning("Please upload data and split it before visualizing.")


    elif page == 'Information':
        display_info()


if __name__ == '__main__':
    main()