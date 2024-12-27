# Importar librerías
import pandas as pd
import numpy as np

"""Load, clean and preprocess the data"""

def main():

    # Load data
    df1 = pd.read_csv("../data/raw/transacciones-1.csv")
    df2 = pd.read_csv("../data/raw/transacciones-2.csv")

    # Concatenate the dataframes
    transactions = pd.concat([df1, df2,], axis=0, ignore_index=True)
    print("The dataset has been loaded succesfully\n")

     # Check for the dataset
    # Display all columns
    pd.set_option('display.max_columns', None)
    
    print("Printing the first 10 rows\n")
    print(transactions.head(11))
    
    # Reset the display settings
    pd.reset_option('display.max_columns')

    # Check for data types
    print("The dataset has the following data types:\n")
    transactions.info()
    
    # Check for missing values
    print("Checking for missing values\n")
    print(transactions.isna().sum())


if __name__ == "__main__":
    main()