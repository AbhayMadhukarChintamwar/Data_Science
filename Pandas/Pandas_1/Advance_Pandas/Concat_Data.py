import pandas as pd

df = pd.read_xml('it_finance_data.xml')
# print(df)



# Concat --> concat data

concat_df1 = df[['Employee_ID', 'Name', 'Company','City']][0:5]
print(concat_df1)

            #    Employee_ID        Name     Company       City
            # 0            1  Employee_1  Microsoft      Mumbai
            # 1            2  Employee_2      Amazon       Pune
            # 2            3  Employee_3         TCS  Hyderabad
            # 3            4  Employee_4  Microsoft        Pune
            # 4            5  Employee_5   Accenture       Pune


concat_df2 = df[['Employee_ID', 'Name', 'Company','City']][5:10]
print(concat_df2)


            #    Employee_ID         Name    Company       City
            # 5            6   Employee_6     Google  Bangalore
            # 6            7   Employee_7     Google     Mumbai
            # 7            8   Employee_8  Accenture     Mumbai
            # 8            9   Employee_9     Amazon       Pune
            # 9           10  Employee_10     Amazon  Bangalore

concat_Data = pd.concat([concat_df1,concat_df2])
print(concat_Data)

            #    Employee_ID         Name     Company       City
            # 0            1   Employee_1  Microsoft      Mumbai
            # 1            2   Employee_2      Amazon       Pune
            # 2            3   Employee_3         TCS  Hyderabad
            # 3            4   Employee_4  Microsoft        Pune
            # 4            5   Employee_5   Accenture       Pune
            # 5            6   Employee_6      Google  Bangalore
            # 6            7   Employee_7      Google     Mumbai
            # 7            8   Employee_8   Accenture     Mumbai
            # 8            9   Employee_9      Amazon       Pune
            # 9           10  Employee_10      Amazon  Bangalore


concat_Data = pd.concat([concat_df1,concat_df2], axis=1)
print(concat_Data)

            #    Employee_ID        Name     Company       City  Employee_ID         Name    Company       City
            # 0          1.0  Employee_1  Microsoft      Mumbai          NaN          NaN        NaN        NaN
            # 1          2.0  Employee_2      Amazon       Pune          NaN          NaN        NaN        NaN
            # 2          3.0  Employee_3         TCS  Hyderabad          NaN          NaN        NaN        NaN
            # 3          4.0  Employee_4  Microsoft        Pune          NaN          NaN        NaN        NaN
            # 4          5.0  Employee_5   Accenture       Pune          NaN          NaN        NaN        NaN
            # 5          NaN         NaN         NaN        NaN          6.0   Employee_6     Google  Bangalore
            # 6          NaN         NaN         NaN        NaN          7.0   Employee_7     Google     Mumbai
            # 7          NaN         NaN         NaN        NaN          8.0   Employee_8  Accenture     Mumbai
            # 8          NaN         NaN         NaN        NaN          9.0   Employee_9     Amazon       Pune
            # 9          NaN         NaN         NaN        NaN         10.0  Employee_10     Amazon  Bangalore



