# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:49 2024

@author: chris
"""

# Learning how to import excel data

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 - number
 1   Gender   11 non-null     object - pandas indetification of string
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
None
"""

print(file.describe())

"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""

#import 2nd dataset
file2 = pandas.read_csv("diab_data.csv")

print(file2)

print(file2.info())

print(file2.describe())

#import 3rd dataset (this one doesn't have column headings)
column_names = ["a","b","c","d","e","f","g","h","i","j","k"]
file3 = pandas.read_csv("housing_data.csv",names = column_names) # can include column names using the additional part of the function

print(file3)

print(file3.info())

print(file3.describe())

#import 4th dataset
file4 = pandas.read_csv("insurance_data.csv",skiprows=5) #must skip meta data here, as it has different size to rest of text

print(file4)

print(file4.info())

print(file4.describe())


#import 5th dataset
file5 = pandas.read_csv("iris.csv")

print(file5)

print(file5.info())

print(file5.describe())

# file = pandas.read_csv("chat_files/iris.csv") to call a file in the directory chat_files