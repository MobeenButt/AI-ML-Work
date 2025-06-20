# Series
# They are one-dimensional labeled arrays capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. Pandas Series is like a column in a table.
import pandas as pd

# Series using list

x=[3,4,5,6,7,8]
index=['a','b','c','d','e','f']
var =pd.Series(x,index,dtype='float',name='Python')
print(var)
print(type(var))
print(var['d'])


# Series using dictionary
dic={"name":['python','java','c++'],"por":[12,13,14,15],"rank":[1,4,2,3]}
var1=pd.Series(dic)
print(var1)

var2=pd.Series(12,index=[1,2,3,4,5,6,7])
print(var2)
print(type(var2))

var3=pd.Series(12,index=[1,2,3,4,5,6,7])
var4=pd.Series(12,index=[1,2,3,4])
print(var3+var4) # Missing values are filled with NaN

# Series using numpy array
import numpy as np
arr = np.array([1,2,3,4,5,6])
var5 = pd.Series(arr, index)
print(var5)
