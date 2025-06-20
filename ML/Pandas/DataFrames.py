# DataFrames
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# It is generally the most commonly used pandas object. DataFrames are similar to SQL tables or Excel spreadsheets. DataFrame is generally the most commonly used pandas object.
import pandas as pd 

lis=[1,2,3,4,5,6]
var=pd.DataFrame(lis)
print(var)
print(type(var))


dic={"a":[1,2,"s",4,5],"s":[1,2,"s",4,5],"d":[1,2,"a",4,5],1:[1,2,3,"h",5]}
var1=pd.DataFrame(dic,columns=['a',1,"d"],index=['a','b','c','d','e'])
print(var1)
print(var1["a"][1])  # Accessing multiple columns
print(type(var1))

# In Dictionary if values are of different lengths, it will give error

# a , s are column names