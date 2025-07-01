import pandas as pd 
data = pd.read_csv('E:\\AI\\ML\\Pandas\\matches.csv')

# print(data.drop_duplicates(subset=['city']))

# # for permanent effect
# print(data.drop_duplicates(subset=['city'], inplace=True))

# # keep parameter
# print(data.drop_duplicates(subset=['city'], keep='last'))  # Keep the last occurrence of each duplicate
# print(data.drop_duplicates(subset=['city'], keep=False))  # Drop all duplicates, keeping none



print(data.drop_duplicates(subset=['season'],keep='last'))  # Keep the last occurrence of each duplicate in 'season'
print(data.drop_duplicates('season',keep='last')[['season','winner']].sort_values('season'))  # Keep the last occurrence of each duplicate in 'season' and 'winner'