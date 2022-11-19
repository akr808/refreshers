#Data wrangling with pandas dataframes

import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")
print(df.head())
print(df.dtypes)

#Typecasting columns
df.points.astype(float)

#Descriptive stats
df.describe(include="all") #Get the descriptiove statistics for the dataframe

#Select columns of a particular data type
df.select_dtypes(object) #Select all object columns
df.select_dtypes(int) #Selects all int columns

#Selecting a subset of columns
df[['country', 'description', 'designation']] #Selection of a subset of columns by name
df.iloc[:,[2,3,4]] #Selection the column with their column index

#Filter columns and rows
df[df.country.isin(['France','Germany'])] #Filter rows with a condition "in"
df[[colnames for colnames in df.columns if 's' in colnames]] #Filter the columns based on some condition

#Groupby and multiple operations
df.groupby("country").points.aggregate(['sum','min','max','mean','median']) #Function aggregate
df.groupby("country").points.agg(['sum','min','max','mean','median'])      #Function agg in short
df.groupby(["country","points"]).price.agg(['sum','min','max','mean','median']) #Group by multiple columns


