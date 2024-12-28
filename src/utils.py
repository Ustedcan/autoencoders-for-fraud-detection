import pandas as pd
def concatenate(*dfs):
    """
    This fuction takes difrent dataframes and concatenates them into one dataframe.
    axis=0 is used to concatenate the dataframes vertically.

    *dfs insted of df1, df2, df3, ... dfn, *dfs is used to allow a variable number of arguments.

    Args:
    - *dfs: a variable number of pandas dataframes

    Returns:
    - A pandas dataframe that contains all the dataframes in *dfs concatenated vertically.   
    
    Example:
    -------------
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    
    result = concatenate(df1, df2)
    print(result)
    """
    return pd.concat(dfs, axis=0, ignore_index=True)