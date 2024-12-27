# Importar librerías
import pandas as pd
import numpy as np

"""Load, clean and preprocess the data"""

def main():

    # Load data
    transactions = pd.read_csv("../data/raw/transacciones.csv")
    print("The dataset has been loaded succesfully\n")

    # Check for data types
    print("The dataset has the following data types:\n")
    transactions.info()
    
    # Check for missing values
    print("Checking for missing values\n")
    print(transactions.isna().sum())

    # Check for the dataset
    # Display all columns
    pd.set_option('display.max_columns', None)
    
    print("Printing the first 10 rows\n")
    print(transactions.head(11))
    
    # Reset the display settings
    pd.reset_option('display.max_columns')

if __name__ == "__main__":
    main()