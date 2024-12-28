import pandas as pd
def concatenate(*dfs):
    """
    This fuction takes difrent dataframes and concatenates them into one dataframe.
    axis=0 is used to concatenate the dataframes vertically.

    Args:
    - *dfs: a variable number of pandas dataframes

    Returns:
    - A pandas dataframe that contains all the dataframes in *dfs concatenated vertically.    
    """
    return pd.concat(dfs, axis=0, ignore_index=True)