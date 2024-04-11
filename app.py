import streamlit as st
import pandas as pd

def load_data(file):
    data = pd.read_csv(file)
    return data

def display_data(data):
    st.write("Data Table:")
    st.write(data)

def main():
    st.title('Data Upload ')

    # select file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "data"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        display_data(data)

if __name__ == '__main__':
    main()
