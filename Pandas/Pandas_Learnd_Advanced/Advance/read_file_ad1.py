import pandas as pd

df = pd.read_csv('finance_big_data.csv')

# print(df.head())


# Create a column Ratio which represents the 'Ratio' of a word

df['Ratio']=df['Total_Value']/df['Price']
print(df.head())

                #          Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value  Ratio
                # 0  2020-10-23     Wipro  Finance              Buy  4965.44       257   1276118.08  257.0
                # 1  2020-03-17  Reliance  Banking             Sell  1163.57       620    721413.40  620.0
                # 2  2021-06-06   Infosys  Finance              Buy   569.79       125     71223.75  125.0
                # 3  2020-05-19       TCS       IT              Buy  4821.96       131    631676.76  131.0
                # 4  2023-05-31  Reliance  Finance             Sell   795.51       336    267291.36  336.0


#  Which is maximum value of Ratio
print(df['Ratio'].max())  # 1000.0000000000001



# What is the one with highest Ratio ?
print(df.sort_values(by='Ratio',ascending=False).head())

                #              Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value   Ratio
                # 99986  2022-12-13     Wipro       IT              Buy   269.34      1000     269340.0  1000.0
                # 91657  2022-04-14       TCS  Finance              Buy   139.45      1000     139450.0  1000.0
                # 85016  2020-05-23       TCS       IT             Sell  2156.49      1000    2156490.0  1000.0
                # 54072  2020-06-29     ICICI   Energy              Buy  4135.07      1000    4135070.0  1000.0
                # 8435   2023-08-16  Reliance  Banking              Buy  2690.20      1000    2690200.0  1000.0

print(df['Ratio'].value_counts())


            # Ratio
            # 8.0      125
            # 2.0      120
            # 261.0    118
            # 267.0    115
            # 64.0     112
            #         ...
            # 926.0      1
            # 61.0       1
            # 152.0      1
            # 281.0      1
            # 953.0      1
            # Name: count, Length: 3008, dtype: int64


# How many words have a Ratio 267.0?  //115

print(df[df['Ratio']==267.0].shape)  # (115, 8)

print(df.query('Ratio == 267.0').shape)  # (115, 8)


# What is the maximum Price of the words with a Ratio 267.0?   // 4979.3

print(df.query('Ratio ==  267.0').sort_values(by='Price', ascending = False).head())

            #              Date   Company   Sector Transaction_Type    Price  Quantity  Total_Value  Ratio
            # 63258  2020-06-11      HDFC  Banking             Sell  4979.30       267   1329473.10  267.0
            # 9437   2023-12-18  Reliance   Energy              Buy  4965.20       267   1325708.40  267.0
            # 55723  2021-03-24     ICICI  Banking             Sell  4890.03       267   1305638.01  267.0
            # 28199  2021-09-26     ICICI  Finance              Buy  4888.95       267   1305349.65  267.0
            # 67625  2022-11-08      HDFC  Banking             Sell  4820.41       267   1287049.47  267.0

print(df.loc[df['Ratio']==267.0,'Price'].max())  # 4979.3
