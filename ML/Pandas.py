import pandas as pd
import numpy as np

labels=['a','b','c','d']
my_data=[10,20,30,40]
arr=np.array(my_data)

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