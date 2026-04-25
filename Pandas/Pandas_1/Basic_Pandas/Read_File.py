import pandas as pd

df = pd.read_csv('finance_big_data.csv')
print(df)
print()

            #              Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value
            # 0      2020-10-23     Wipro  Finance              Buy  4965.44       257   1276118.08
            # 1      2020-03-17  Reliance  Banking             Sell  1163.57       620    721413.40
            # 2      2021-06-06   Infosys  Finance              Buy   569.79       125     71223.75
            # 3      2020-05-19       TCS       IT              Buy  4821.96       131    631676.76
            # 4      2023-05-31  Reliance  Finance             Sell   795.51       336    267291.36
            # ...           ...       ...      ...              ...      ...       ...          ...
            # 99995  2020-10-25       TCS  Banking             Sell  2327.18       340    791241.20
            # 99996  2021-12-21       TCS   Energy             Sell  4973.21       937   4659897.77
            # 99997  2021-11-21  Reliance  Banking             Sell  3571.17       971   3467606.07
            # 99998  2020-01-22       TCS       IT             Sell  4961.80       557   2763722.60
            # 99999  2021-05-27  Reliance  Finance              Buy  1468.79       408    599266.32

            # [100000 rows x 7 columns]
            # <class 'pandas.DataFrame'>
            # RangeIndex: 100000 entries, 0 to 99999
            # Data columns (total 7 columns):


df_head = df.head()
print(df_head)
print()

            #        Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value
            # 0  2020-10-23     Wipro  Finance              Buy  4965.44       257   1276118.08
            # 1  2020-03-17  Reliance  Banking             Sell  1163.57       620    721413.40
            # 2  2021-06-06   Infosys  Finance              Buy   569.79       125     71223.75
            # 3  2020-05-19       TCS       IT              Buy  4821.96       131    631676.76
            # 4  2023-05-31  Reliance  Finance             Sell   795.51       336    267291.36

            # <class 'pandas.DataFrame'>
            # RangeIndex: 100000 entries, 0 to 99999
            # Data columns (total 7 columns):

            #  #   Column            Non-Null Count   Dtype
            # ---  ------            --------------   -----
            #  0   Date              100000 non-null  str
            #  1   Company           100000 non-null  str
            #  2   Sector            100000 non-null  str
            #  3   Transaction_Type  100000 non-null  str
            #  4   Price             100000 non-null  float64
            #  5   Quantity          100000 non-null  int64
            #  6   Total_Value       100000 non-null  float64
            # dtypes: float64(2), int64(1), str(4)
            # memory usage: 5.3 MB


df_tail = df.tail()
print(df_tail)
print()

            #              Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value
            # 99995  2020-10-25       TCS  Banking             Sell  2327.18       340    791241.20
            # 99996  2021-12-21       TCS   Energy             Sell  4973.21       937   4659897.77
            # 99997  2021-11-21  Reliance  Banking             Sell  3571.17       971   3467606.07
            # 99998  2020-01-22       TCS       IT             Sell  4961.80       557   2763722.60
            # 99999  2021-05-27  Reliance  Finance              Buy  1468.79       408    599266.32

            # <class 'pandas.DataFrame'>
            # RangeIndex: 100000 entries, 0 to 99999
            # Data columns (total 7 columns):

            #  #   Column            Non-Null Count   Dtype
            # ---  ------            --------------   -----
            #  0   Date              100000 non-null  str
            #  1   Company           100000 non-null  str
            #  2   Sector            100000 non-null  str
            #  3   Transaction_Type  100000 non-null  str
            #  4   Price             100000 non-null  float64
            #  5   Quantity          100000 non-null  int64
            #  6   Total_Value       100000 non-null  float64
            # dtypes: float64(2), int64(1), str(4)
            # memory usage: 5.3 MB


df_info = df.info()
print(df_info)
print()

            #    Column            Non-Null Count   Dtype
            # ---  ------            --------------   -----
            #  0   Date              100000 non-null  str
            #  1   Company           100000 non-null  str
            #  2   Sector            100000 non-null  str
            #  3   Transaction_Type  100000 non-null  str
            #  4   Price             100000 non-null  float64
            #  5   Quantity          100000 non-null  int64
            #  6   Total_Value       100000 non-null  float64
            # dtypes: float64(2), int64(1), str(4)
            # memory usage: 5.3 MB
            # None


df_columns = df.columns
print(df_columns)
print()
            # Index(['Date', 'Company', 'Sector', 'Transaction_Type', 'Price', 'Quantity',
            #        'Total_Value'],
            #       dtype='str')


find_Index = df['Price']
print(find_Index)
print()

            # 0        4965.44
            # 1        1163.57
            # 2         569.79
            # 3        4821.96
            # 4         795.51
            #           ...
            # 99995    2327.18
            # 99996    4973.21
            # 99997    3571.17
            # 99998    4961.80
            # 99999    1468.79
            # Name: Price, Length: 100000, dtype: float64


