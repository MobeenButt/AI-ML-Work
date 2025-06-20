# DataFrames
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# It is generally the most commonly used pandas object. DataFrames are similar to SQL tables or Excel spreadsheets. DataFrame is generally the most commonly used pandas object.
import pandas as pd 

lis=[1,2,3,4,5,6]
var=pd.DataFrame(lis)
print(var)
print(type(var))