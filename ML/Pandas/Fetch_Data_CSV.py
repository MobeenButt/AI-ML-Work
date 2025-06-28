import pandas as pd 
import numpy as np

data=pd.read_csv('E:\AI\ML\Pandas\\matches.csv')
# print(data) 
# print(type(data[['winner','team1','team2']]) ) 


# iloc
print(data.iloc[0:2]) 
print(data.iloc[0:2, 0:3])  # Accessing first two rows and first three columns