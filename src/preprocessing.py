# Import the required libraries
import pandas as pd
import numpy as np
from utils import concatenate

"""Load, clean and preprocess the data"""

def main():

    # Load data
    df1 = pd.read_csv("../data/raw/transacciones-1.csv")
    df2 = pd.read_csv("../data/raw/transacciones-2.csv")

    # Apply the fucntion concatenate
    transactions = concatenate(df1, df2)
    print(transactions)        

    # Drop duplicates
    duplicates = transactions.duplicated().sum()
    transactions = transactions.drop_duplicates()
    print("Duplicates have been removed\n")
    print(f"{duplicates} were removed\n")


if __name__ == "__main__":
    main()