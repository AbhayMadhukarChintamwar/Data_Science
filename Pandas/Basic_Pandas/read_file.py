import pandas as pd


df = pd.read_csv("finance_big_data.csv")

print('Head of data : ')
print(df.head())

            # output:

            #       Date   Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 0  2020-10-17   Infosys  Banking              Buy  81.49         1        81.49
            # 1  2020-09-10      HDFC       IT             Sell  85.20         1        85.20
            # 2  2022-08-11  Reliance       IT             Sell  75.56         2       151.12
            # 3  2021-03-23     ICICI  Finance             Sell  73.30        10       733.00
            # 4  2023-12-29     ICICI   Energy             Sell  88.72        10       887.20

print('Print info about data: ')
print(df.info())


            # output:

            # <class 'pandas.DataFrame'>
            # RangeIndex: 100 entries, 0 to 99
            # Data columns (total 7 columns):
            #     Column            Non-Null Count  Dtype
            # ---  ------            --------------  -----
            #  0   Date              100 non-null    str
            #  1   Company           100 non-null    str
            #  2   Sector            100 non-null    str
            #  3   Transaction_Type  100 non-null    str
            #  4   Price             100 non-null    float64
            #  5   Quantity          100 non-null    int64
            #  6   Total_Value       100 non-null    float64
            # dtypes: float64(2), int64(1), str(4)
            # memory usage: 5.6 KB
            # None

print('shape')
print(df.shape) # (100, 7)

print('print date range using df.loc : ')
print(df.loc[0:99, "Date"])


            # output:

            # 0     2020-10-17
            # 1     2020-09-10
            # 2     2022-08-11
            # 3     2021-03-23
            # 4     2023-12-29
            #          ...
            # 95    2020-09-16
            # 96    2023-05-24
            # 97    2020-10-08
            # 98    2020-07-04
            # 99    2022-07-08
            # Name: Date, Length: 100, dtype: str

print('df.loc Value : ')
print(df.loc[:, "Transaction_Type"])

            # output:

            # 0      Buy
            # 1     Sell
            # 2     Sell
            # 3     Sell
            # 4     Sell
            #       ...
            # 95    Sell
            # 96     Buy
            # 97     Buy
            # 98     Buy
            # 99    Sell
            # Name: Transaction_Type, Length: 100, dtype: str

# What is the highest price in the dataset?

max_Price = df['Price'].max()

print('Maximum Price :')
print(max_Price)  # 99.82

print('Maximum : ')
print(df.max())

            # output:
            # Date                2024-02-05
            # Company                  Wipro
            # Sector                      IT
            # Transaction_Type          Sell
            # Price                    99.82
            # Quantity                    10
            # Total_Value              986.4
            # dtype: object

print('Minimum :')
print(df.min())

            # output:

            # Date                2020-01-08
            # Company                   HDFC
            # Sector                 Banking
            # Transaction_Type           Buy
            # Price                    50.06
            # Quantity                     1
            # Total_Value              52.96
            # dtype: object


print('Mean Price: ')
print(df['Price'].mean()) #73.5517



# DataFrame() constructor is used to create a DataFrame from a dictionary, list, or another DataFrame.
data = pd.DataFrame(df)
print('DataFrame: ')
print(data)

            # output:
            #           Date   Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 0   2020-10-17   Infosys  Banking              Buy  81.49         1        81.49
            # 1   2020-09-10      HDFC       IT             Sell  85.20         1        85.20
            # 2   2022-08-11  Reliance       IT             Sell  75.56         2       151.12
            # 3   2021-03-23     ICICI  Finance             Sell  73.30        10       733.00
            # 4   2023-12-29     ICICI   Energy             Sell  88.72        10       887.20
            # ..         ...       ...      ...              ...    ...       ...          ...
            # 95  2020-09-16   Infosys  Finance             Sell  99.82         5       499.10
            # 96  2023-05-24       TCS  Finance              Buy  96.58         3       289.74
            # 97  2020-10-08     ICICI       IT              Buy  96.46        10       964.60
            # 98  2020-07-04      HDFC       IT              Buy  59.32         3       177.96
            # 99  2022-07-08      HDFC  Banking             Sell  57.25         5       286.25



# describe() method gives us the statistical summary of the DataFrame
describe_data = df.describe()

print('Describe data : ')
print(describe_data)


            # output:
            #            Price    Quantity  Total_Value
            # count  100.000000  100.000000   100.000000
            # mean    73.551700    5.570000   410.165100
            # std     14.619988    3.075662   248.022353
            # min     50.060000    1.000000    52.960000
            # 25%     61.070000    3.000000   194.695000
            # 50%     73.475000    5.000000   397.930000
            # 75%     85.392500    8.000000   544.700000
            # max     99.820000   10.000000   986.400000

df.loc[:, "char_count"] = df["Company"].str.len()

print(df)

            # output:

            #         Date   Company   Sector Transaction_Type  Price  Quantity  Total_Value  char_count
            # 0   2020-10-17   Infosys  Banking              Buy  81.49         1        81.49           7
            # 1   2020-09-10      HDFC       IT             Sell  85.20         1        85.20           4
            # 2   2022-08-11  Reliance       IT             Sell  75.56         2       151.12           8
            # 3   2021-03-23     ICICI  Finance             Sell  73.30        10       733.00           5
            # 4   2023-12-29     ICICI   Energy             Sell  88.72        10       887.20           5
            # ..         ...       ...      ...              ...    ...       ...          ...         ...
            # 95  2020-09-16   Infosys  Finance             Sell  99.82         5       499.10           7
            # 96  2023-05-24       TCS  Finance              Buy  96.58         3       289.74           3
            # 97  2020-10-08     ICICI       IT              Buy  96.46        10       964.60           5
            # 98  2020-07-04      HDFC       IT              Buy  59.32         3       177.96           4
            # 99  2022-07-08      HDFC  Banking             Sell  57.25         5       286.25           4

            # [100 rows x 8 columns]

print("Duplicated : ")
print(df.duplicated('Price'))

print("Duplicated : ")
print(df.duplicated('Company'))

print("Duplicated : ")
print(df.duplicated('Total_Value'))