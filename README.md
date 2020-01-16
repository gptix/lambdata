# Welcome to Lambdata!

This is a high-quality README.md file:
- It is skimmable
- It will have appropriate examples, details, and links for someone 
who wants to understand the code in this repo.

## Overview

This repository is work done as part of instruction for Lambda School 
Data Science Cohort 10 (**Go Laser Sharks!**).

## Objectives

Work this week has been to familiarize students with 
- using the command line,
- packaging code as a module,
- versioning module revisions,
- compiling modules using **twine**,
- pushing modules to repositories,
- using PEP8 to adhere to stylistic conventions
- object-oriented programming,
- and unit tests.

### The ```/lambdata-gptix``` directory / folder / sub-repo

This exists to serve as a container, with usable name via 
 ```pip install```, to hold files that hold code for things to be imported.

### ```__Init__.py```

An ```__init__.py``` file was made, including a couple of definitions 
that obtain throughout the module.

## ```def_utils.py```
A file was created to show how to package functions so that, once a
module is installed, a function can be used.


## ```setup.py``` 
This file is used when packaging code for upload to test.pypi.

# Using this module:
```$ pip install lambdata-gptix as gpt
# with X being a matrix of features, and y being a vector of targets,
# create subsets for training, validation, and testing.
$ X_train, X_val, X_test, y_train, y_val, y_test = gpt.def train_val_test_split(X, y)
$ gpt.train_val_test_split --help

# With df being a pandas dataframe, and mylist being a list of values to
# add to df as a Series/column (the lengths of df and mylist being equal),
# return a dataframe that is df with mylist appended as a new Series/column.
$ df = pandas.DataFrame([[1, 2], [3, 4], [5, 6]])
$ mylist = ['cat', 'dog', 'sparrow']
$ foo =  gpt.add_list_to_frame(df, mylist)
$ foo
$ gpt.add_list_to_frame --help
