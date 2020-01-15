"""
Utilities fuctions for working with DataFrames.
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def train_val_test_split(X, y):
        """
Split arrays or matrices into random train, validation, and test subsets.
Wraps sklearn.model_selection.train_test_split.
Split is currently hard-coded as 25% train, 50% validate, 25% test.
"""
# TODO - allow specification of sizes as fractions.
#   TODO - validate specified inputs (if all specified, must add to 1;
        #          if not all, calculate remainder

        # Split inputs, X_val and y_val are final.
        X_temp, X_val, y_temp, y_val = train_test_split(X, y, train_size=0.5)
        # Split X_temp and y_temp again.
        X_train, X_test, y_train, y_test =
        train_test_split(X_temp, y_temp, train_size=0.5)

        return X_train, X_val, X_test, y_train, y_val, y_test


def add_list_to_frame(dataframe, lst, colname):
        """
Add a list as a new column in a dataframe, with specified column name.
"""
# TODO - validate lengths of dataframe and list. Maybe error.
        dataframe[colname] = lst
        return dataframe
