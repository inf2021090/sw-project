import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.info import display_info
from ml import *

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
    
    return data, X, y

def main():
    st.title('Data Upload and Display')

    # Sidebar navigation
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Upload Data', 'Information', 'Data Visualization'))

    if page == 'Upload Data':
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

        data, X, y = split_data(data)
        display_data(data)  # Call display_data function

    elif page == 'Data Visualization':
        if 'data' not in st.session_state:
            st.warning("Please upload a file first in the 'Upload Data' section.")
        else:
            visualize_dataset(st.session_state.data)

    elif page == 'Information':
        display_info()  

if __name__ == '__main__':
    main()
