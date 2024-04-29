#Numpy--Numerical Python
# Python arrays differ from lists

#Numpy-array oriented programming, has smaller memory consumption, better runtime and ease of data manipulation.

import numpy as np

#define a list
distance=[1,13.1,26.2,100]
print(type(distance))

numpy_dist=np.array(distance)
print(type(numpy_dist))
print(numpy_dist)

conversion1=numpy_dist*1.609334
print (conversion1)

conversion2=[]
for x in distance:
    conversion2.append(x*1.609334)

print (conversion2)

import pandas as pd

#Pandas built on Numpy
#Fundamental pandas data structures: Series, DataFrame, Panel

#A dataframe is the way the pandas library in pyhton represents tabular data
# Like a powerful spreadsheet within the code
# Rows: Each row represents a single observation or data point
#Columns: each column represents a variable or feature

#############         Exploring Datasets            ######################3
url='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df=pd.read_csv(url)

print(df.head())
print("\n")

print(df.tail())
print("\n")

print(df.shape)
print("150 rows and 5 columns")
print("\n")

print(df.info())
print("\n")

print(df.describe())
print("\n")

print(df.columns)
print("\n")

#####################     Manipulating Data       ###################
# Selecting columns
df_selected=df[['species','petal_length']]
print(df_selected)
print("\n")

#Filtering ROws
df_setosa=df[df['species']=='setosa']
print(df_setosa)
print("\n")

# Creating new columns
df['petal area']=df['petal_length']*df['petal_width']
print(df['petal area'])
print("\n")

#Renaming/dropping
df=df.rename(columns={'sepal_length':'sepal_len'})
print(df.columns)
print("\n")

#Pandas toolbox
#mean/max/min/std/var/unique()

#Grouping and Aggregation
#df.groupby(): Divide data based on categories ina column
print(df['petal area'].mean())
print(df['species'].nunique())
print(df.groupby('species')['petal_length'].std())

#.agg(): apply calculations within each group 
print(df.groupby('species').agg(
    mean_petal_length=('petal_length','mean'),
    max_sepal_width=('sepal_width','max')
))
