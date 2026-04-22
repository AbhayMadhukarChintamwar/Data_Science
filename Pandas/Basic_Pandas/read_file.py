import pandas as pd

df = pd.read_csv("finance_small_data.csv")
# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.loc[0:99, "Date"])
# print(df.loc[:, "Transaction_Type"])

# What is the highest price in the dataset?
max_Price = df['Price'].max()
print(max_Price)
print(df.max())
print(df.min())
print(df['Price'].mean())

data = pd.DataFrame(df)
print(data)