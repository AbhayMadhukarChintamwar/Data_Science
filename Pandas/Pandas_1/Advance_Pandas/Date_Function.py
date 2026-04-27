import pandas as pd

date = pd.date_range(start= '2002-03-08', end='2007-06-21')
print(date)
print()

            # DatetimeIndex(['2002-03-08', '2002-03-09', '2002-03-10', '2002-03-11',
            #                '2002-03-12', '2002-03-13', '2002-03-14', '2002-03-15',
            #                '2002-03-16', '2002-03-17',
            #                ...
            #                '2007-06-12', '2007-06-13', '2007-06-14', '2007-06-15',
            #                '2007-06-16', '2007-06-17', '2007-06-18', '2007-06-19',
            #                '2007-06-20', '2007-06-21'],
            #               dtype='datetime64[us]', length=1932, freq='D')



df_date = pd.DataFrame({'Date':date})
print(df_date)
print()

            #            Date
            # 0    2002-03-08
            # 1    2002-03-09
            # 2    2002-03-10
            # 3    2002-03-11
            # 4    2002-03-12
            # ...         ...
            # 1927 2007-06-17
            # 1928 2007-06-18
            # 1929 2007-06-19
            # 1930 2007-06-20
            # 1931 2007-06-21

            # [1932 rows x 1 columns]



df = pd.DataFrame({'date':['2002-03-08','1993-10-13','2023-04-16','2007-06-21']})
print(df)
print(df.dtypes)
print()

            #         date
            # 0  2002-03-08
            # 1  1993-10-13
            # 2  2023-04-16
            # 3  2007-06-21
            # date    str
            # dtype: object




df['update_date'] = pd.to_datetime(df['date'])
print(df)
print(df.dtypes)
print()

            #          date update_date
            # 0  2002-03-08  2002-03-08
            # 1  1993-10-13  1993-10-13
            # 2  2023-04-16  2023-04-16
            # 3  2007-06-21  2007-06-21
            # date                      str
            # update_date    datetime64[us]
            # dtype: object


df['Year']  = df['update_date'].dt.year
print(df)
print()


            #          date update_date  Year
            # 0  2002-03-08  2002-03-08  2002
            # 1  1993-10-13  1993-10-13  1993
            # 2  2023-04-16  2023-04-16  2023
            # 3  2007-06-21  2007-06-21  2007

df['Month']  = df['update_date'].dt.month
print(df)
print()

            #          date update_date  Year  Month
            # 0  2002-03-08  2002-03-08  2002      3
            # 1  1993-10-13  1993-10-13  1993     10
            # 2  2023-04-16  2023-04-16  2023      4
            # 3  2007-06-21  2007-06-21  2007      6



df['Day']  = df['update_date'].dt.day
print(df)
print()

            #          date update_date  Year  Month  Day
            # 0  2002-03-08  2002-03-08  2002      3    8
            # 1  1993-10-13  1993-10-13  1993     10   13
            # 2  2023-04-16  2023-04-16  2023      4   16
            # 3  2007-06-21  2007-06-21  2007      6   21
