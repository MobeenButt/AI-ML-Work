import pandas as pd

delivery = pd.read_csv('E:\\AI\\ML\\Pandas\\deliveries.csv')
# print(delivery.head(2)) 


runs=delivery.groupby('batsman')
runs.get_group('V Kohli')
# print(runs.get_group('V Kohli'))  # Get all deliveries by V Kohli
# print(runs.get_group('V Kohli').shape)  # Get the shape of the DataFrame for V Kohli
# print(runs['batsman_runs'].sum().sort_values(ascending=False))  # Sum of all batsmen names (not meaningful, but shows how to use sum)


#  for 6 runs
six_runs = delivery['batsman_runs'] == 6
new_runs = delivery[six_runs]
# print(new_runs.shape)  # Get the shape of the DataFrame for 6 runs

print(new_runs.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False))
# for git changes