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

    # Drop duplicates
    duplicates = transactions.duplicated().sum()
    print("Duplicates have been removed\n")
    print(f"{duplicates} were removed\n")


if __name__ == "__main__":
    main()