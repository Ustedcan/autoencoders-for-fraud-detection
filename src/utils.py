import pandas as pd

def concatenate(*dfs):
    """
    Concatenates multiple dataframes vertically.

    Args:
    - *dfs: Variable number of pandas dataframes.

    Returns:
    - A pandas dataframe with all input dataframes concatenated vertically.
    """
    return pd.concat(dfs, axis=0, ignore_index=True)