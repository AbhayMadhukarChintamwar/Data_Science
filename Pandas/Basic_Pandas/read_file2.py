import pandas as pd

df = pd.read_csv('finance_small_data.csv')
dataframe = pd.DataFrame(df)
print(dataframe)

# sort
sort = df.sort_values(by=['Total_Value'],ascending=False)
print('Sort the total value in descending order : ')
print(sort)

            # Sort the total value in descending order :
            #           Date   Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 56  2021-10-03   Infosys  Finance             Sell  98.64        10       986.40
            # 7   2023-02-22  Reliance       IT             Sell  97.61        10       976.10
            # 97  2020-10-08     ICICI       IT              Buy  96.46        10       964.60
            # 74  2024-01-10     Wipro       IT             Sell  92.06        10       920.60
            # 5   2022-09-01     ICICI  Banking             Sell  91.59        10       915.90
            # ..         ...       ...      ...              ...    ...       ...          ...
            # 13  2021-02-11     ICICI   Energy             Sell  61.79         1        61.79
            # 58  2023-02-05      HDFC  Finance              Buy  58.90         1        58.90
            # 82  2020-09-05   Infosys  Finance             Sell  57.58         1        57.58
            # 62  2020-04-21  Reliance   Energy             Sell  56.86         1        56.86
            # 83  2023-04-25  Reliance  Finance             Sell  52.96         1        52.96

            # [100 rows x 7 columns]


print(df.loc[df['Total_Value']==986.40])

            #          Date  Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 56  2021-10-03  Infosys  Finance             Sell  98.64        10        986.4

print(df['Total_Value']==733.00)

            # 0     False
            # 1     False
            # 2     False
            # 3      True
            # 4     False
            #       ...
            # 95    False
            # 96    False
            # 97    False
            # 98    False
            # 99    False
            # Name: Total_Value, Length: 100, dtype: bool


# What is the most common total value
print(df['Price'].describe())


            # count    100.000000
            # mean      73.551700
            # std       14.619988
            # min       50.060000
            # 25%       61.070000
            # 50%       73.475000
            # 75%       85.392500
            # max       99.820000
            # Name: Price, dtype: float64


print(df['Price'].mode())
            # 0    89.77
            # Name: Price, dtype: float64



# value_counts()
print(df['Price'].value_counts().head())

            # Price
            # 89.77    2
            # 81.49    1
            # 85.20    1
            # 75.56    1
            # 73.30    1
            # Name: count, dtype: int64


print(df.loc[df['Company']=='Infosys'].head(10))

            #           Date  Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 0   2020-10-17  Infosys  Banking              Buy  81.49         1        81.49
            # 9   2020-09-12  Infosys  Banking              Buy  89.77         7       628.39
            # 20  2020-02-22  Infosys  Finance             Sell  73.07         5       365.35
            # 22  2023-06-09  Infosys  Finance              Buy  53.76         2       107.52
            # 23  2020-03-18  Infosys   Energy              Buy  63.38         1        63.38
            # 42  2023-08-10  Infosys       IT              Buy  96.05         6       576.30
            # 54  2023-10-18  Infosys  Finance              Buy  89.72         2       179.44
            # 56  2021-10-03  Infosys  Finance             Sell  98.64        10       986.40
            # 57  2023-06-05  Infosys       IT              Buy  52.28         8       418.24
            # 61  2022-06-05  Infosys       IT              Buy  79.88         1        79.88


print(df.loc[df['Company']=='Infosys'].sort_values(by='Sector'))

            #     Date  Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 0   2020-10-17  Infosys  Banking              Buy  81.49         1        81.49
            # 9   2020-09-12  Infosys  Banking              Buy  89.77         7       628.39
            # 80  2020-01-08  Infosys  Banking             Sell  50.39         7       352.73
            # 23  2020-03-18  Infosys   Energy              Buy  63.38         1        63.38
            # 65  2023-03-03  Infosys   Energy             Sell  51.91         3       155.73
            # 84  2021-02-10  Infosys   Energy             Sell  79.82         5       399.10
            # 20  2020-02-22  Infosys  Finance             Sell  73.07         5       365.35
            # 22  2023-06-09  Infosys  Finance              Buy  53.76         2       107.52
            # 54  2023-10-18  Infosys  Finance              Buy  89.72         2       179.44
            # 56  2021-10-03  Infosys  Finance             Sell  98.64        10       986.40
            # 82  2020-09-05  Infosys  Finance             Sell  57.58         1        57.58
            # 95  2020-09-16  Infosys  Finance             Sell  99.82         5       499.10
            # 42  2023-08-10  Infosys       IT              Buy  96.05         6       576.30
            # 57  2023-06-05  Infosys       IT              Buy  52.28         8       418.24
            # 61  2022-06-05  Infosys       IT              Buy  79.88         1        79.88



#  What is the  total shortest (total minimum) value of Infosys

print(df.loc[df['Company']=='Infosys' , 'Total_Value'].min())  # 57.58


print(df.loc[
    (df['Company']=='Infosys') &
    (df['Total_Value']== 57.58)
])

            #          Date  Company   Sector Transaction_Type  Price  Quantity  Total_Value
            # 82  2020-09-05  Infosys  Finance             Sell  57.58         1        57.58


