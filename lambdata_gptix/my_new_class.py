# Define a class of dataframes that can have a new column added.

import pandas as pd
from sklearn.model_selection import train_test_split

class SpecialDataFrame():
    """
    A DataFrame class that makes it easy to add columns of Trues.
    """

    def __init__(self, df):
        self.df = df # Not sure what a default would be.


    def add_trues(self, colname):
        """
        Add a column of 'True's to a Dataframe.
        """
        self.df[colname] = True
        return self.df
