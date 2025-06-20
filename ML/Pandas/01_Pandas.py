import pandas as pd
import numpy as np

labels=['a','b','c','d']
my_data=[10,20,30,40]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30,'d':40}
print(labels)
print(my_data)
print(arr)

# syntax Series(list)
pandas=pd.Series(data=my_data)
print(pandas)

# syntax Series(list=,index=)
pandas1=pd.Series(data=my_data,index=labels)
pandas1=pd.Series(my_data,labels)
print(pandas1)
# both are same
pandas1=pd.Series(my_data,labels)
print(pandas1)

# syntax Series(numpyArryas)
pandas3=pd.Series(arr,labels)
print(pandas3)

# syntax Series(dictionary)
pandas4=pd.Series(d,labels)
print(pandas4)
print(d)

print(pd.Series(data=labels))

print(pd.Series(data=[sum,print,len]))