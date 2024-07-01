import pandas as pd

def load_data(file):
    try:
        file_name = file.name
        # Check if the file is a CSV
        if file_name.endswith('.csv'):
            data = pd.read_csv(file)
        # Check if the file is an Excel file
        elif file_name.endswith('.xlsx'):
            data = pd.read_excel(file)
        # Raise an error for unsupported file formats
        else:
            raise ValueError("Unsupported file format")
        return data
    except Exception as error:
        # Return the error message as a string
        return str(error)