# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:41 2024

@author: chris
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data frames - specific to pandas
"""

import pandas

#import pandas as pd (can then use pd instead of typing pandas the whole time)

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

# Storing data with individual variables
age1 = 30
age2 = 25
age3 = 29

# Storing variables as a list
age = [30, 25, 29]

print(age)
"""
[30, 25, 29]
"""

# 1st element in a list starts at 0
print(age[0])
"""
30
"""

# examples of some built in functions
print(min(age))
"""
25
"""

print(sum(age)/len(age))
"""
28.0
"""

print(age[0:2])
"""
[30, 25]
"""

# can add additional entries to a variable
age.append(100)

print(age)
"""
[30, 25, 29, 100]
"""

# to add the number anywhere in the list, use insert function
age.insert(0, 100)
print(age)

"""
Dictionaries - key:value pairs

cat: "a cute animal"


"""

mammals = {"cat": "a cute animal", "lion": "king of the jungle", "elephant": "a gigantic herbivore"}

print(mammals["cat"])

"""
Data frames


"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
        "fruits": fruits,
        "sizes": size_nm
        }

"""
df = dataframe

convert your dictionary into a dataframe (spreadsheet/matrix etc.)
"""

df = pandas.DataFrame(fruit_sizes)

print(df["fruits"])
print(df["sizes"])
print(df["sizes"].min())
print(df["sizes"].max())
print(df.describe())

# if you want to see which values satisfy the criterion, you have to make a new dataframe, else it just gives true/false
print(df[df["sizes"] > 10])

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

# add a new column to dataframe
df["prices"] = prices

# how to remove a column from a dataframe, need the true to modify the data without retaining a copy of the data
df.drop(columns=["sizes"], inplace=True)
