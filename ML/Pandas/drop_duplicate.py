import pandas as pd 
data = pd.read_csv('E:\\AI\\ML\\Pandas\\matches.csv')

print(data.drop_duplicates(subset=['city']))

# for permanent effect
print(data.drop_duplicates(subset=['city'], inplace=True))