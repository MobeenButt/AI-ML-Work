# Main focus hoga read krna then preview using head and tail functions phir uski shape check krna or information dataset ki using info function jo btay ga k data main kitne rows hain, columns hain, unki data types kya hain, konsa null value hai, kitny non-null values hain, etc.
# Reading CSV files using Pandas

import pandas as pd
import numpy as np
import os
# Analysis if csv data
data = pd.read_csv('E:\AI\ML\Pandas\\matches.csv')
# print(data)

# for just previewing the data head() is used by default it will show 5 rows
print(data.head(3))

# for just previewing the data tail() is used by default it will show 5 rows 
print(data.tail())

print(data.shape)  # shape of the data (rows, columns)

print(data.info())  # information about the data

print(data.describe())  # statistical summary of the data yeh numerical columns ka summary dega jaysy count , mean, std, min, 25%, 50%, 75%, max in ka btata ha  mathematical summary dega


