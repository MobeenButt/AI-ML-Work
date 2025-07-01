import pandas as pd

company = pd.read_csv('E:\\AI\\ML\\Pandas\\fotune.csv')

print(company.head())
sectors=company.groupby('Company Name')
print(sectors.last())  # Get the last entry in each sector
# Count of companies in each sector
print(sectors['Rank'].mean())  # Average rank in each sector
print(len(company)) # total number of rows