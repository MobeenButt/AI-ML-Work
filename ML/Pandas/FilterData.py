import pandas as pd
import numpy as np

# Masking is a way to filter data based on a condition
# For example, if we want to filter data based on a specific city   

data=pd.read_csv('E:\\AI\\ML\\Pandas\\matches.csv')
# print(data)
mask=(data['city']=='Hyderabad')
# print(type(data['city']=='Hyderabad')) #boolean series
# print(data[mask])
# Filtered data where city is Hyderabad

def get_city_match_count(city):
    mask=data['city']==city
    return data[mask].shape[0]

print(get_city_match_count('Hyderabad'))
print(get_city_match_count('Bangalore'))

def get_date_match_count(date):
    mask1=data['city']=='Hyderabad'
    mask2=data['date']>'2010-01-01'
    return data[mask1 & mask2].shape[0]

print(get_date_match_count('2010-01-01'))