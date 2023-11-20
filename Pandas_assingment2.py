# Importing necessary libraries
import pandas as pd

# Importing the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|', index_col='user_id')

# Displaying the first and last 10 entries
print("First 10 entries:")
print(users.head(10))
print("\nLast 10 entries:")
print(users.tail(10))

# Number of observations in the dataset
num_observations = users.shape[0]
print("\nNumber of Observations:", num_observations)

# Number of columns in the dataset
num_columns = users.shape[1]
print("\nNumber of Columns:", num_columns)

# Name of all columns
print("\nColumns:", users.columns)

# Dataset indexing
print("\nDataset Indexing:", users.index)

# Data type of each column
print("\nData Types of Each Column:")
print(users.dtypes)

# Print only the occupation column
print("\nOccupation Column:")
print(users['occupation'])

# Number of different occupations
num_occupations = users['occupation'].nunique()
print("\nNumber of Different Occupations:", num_occupations)

# Most frequent occupation
most_frequent_occupation = users['occupation'].mode()[0]
print("\nMost Frequent Occupation:", most_frequent_occupation)

# Describe all the columns
print("\nDescribe All Columns:")
print(users.describe(include='all'))

# Summarize only the occupation column
print("\nOccupation Summary:")
print(users['occupation'].value_counts())

# Mean age of users
mean_age = users['age'].mean()
print("\nMean Age of Users:", mean_age)

# Age with the least occurrence
least_occurred_age = users['age'].value_counts().idxmin()
print("\nAge with Least Occurrence:", least_occurred_age)
