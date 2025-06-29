import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Value counts is a way to count the number of occurrences of each value in a column

data = pd.read_csv('E:\\AI\\ML\\Pandas\\matches.csv')
# print(data.head())  # Display the first five rows of the DataFrame

# print(data['winner'].value_counts())

# Plot functions

# Bar and barh plots

# print(data['winner'].value_counts().head(5).plot(kind='barh'))
# # now we can plot the value counts of the 'winner' column
# plt.title('Number of Matches Won by Each Team')
# plt.xlabel('Teams')
# plt.ylabel('Number of Matches Won')
# plt.show()


# Pie plot

# print(data['toss_decision'].value_counts())
# print(data['toss_decision'].value_counts().plot(kind='pie'))
# plt.show()


# Histogram Plot    

print(data['win_by_runs'].plot(kind='hist'))
plt.show()