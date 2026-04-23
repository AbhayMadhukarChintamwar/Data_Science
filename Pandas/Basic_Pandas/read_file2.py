import pandas as pd

df = pd.read_csv('finance_small_data.csv')
# dataframe = pd.DataFrame(df)
# print(dataframe)

# sort
sort = df.sort_values(by=['Total_Value'],ascending=False)
print('Sort the total value in descending order : ')
# print(sort)

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

print(df['Total_Value']==986.40)