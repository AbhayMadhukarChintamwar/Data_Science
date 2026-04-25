import pandas as pd

df = pd.read_xml('it_finance_data.xml')
print(df)

#  describe() --> it is only showing integer or float values
described = df.describe()
print(described)
print()

            #       Employee_ID        Salary  Experience_Years
            # count  12000.00000  1.200000e+04      12000.000000
            # mean    6000.50000  1.152899e+06          7.798700
            # std     3464.24595  4.936764e+05          4.171116
            # min        1.00000  3.000730e+05          0.500000
            # 25%     3000.75000  7.248252e+05          4.200000
            # 50%     6000.50000  1.156995e+06          7.800000
            # 75%     9000.25000  1.587310e+06         11.400000
            # max    12000.00000  1.999967e+06         15.000000

print(df.dtypes)
print()

            # Employee_ID           int64
            # Name                    str
            # Department              str
            # Role                    str
            # Company                 str
            # City                    str
            # Salary                int64
            # Experience_Years    float64

dtype: object
add_describe_at_str = df[df.dtypes[df.dtypes=='str'].index].describe()
print(add_describe_at_str)
print()

            #               Name Department               Role   Company   City
            # count        12000      12000              12000     12000  12000
            # unique       12000          2                 10         8      5
            # top     Employee_1         IT  Financial Analyst  Deloitte   Pune
            # freq             1       6008               1239      1603   2491

print(df[['Salary']])

            #        Salary
            # 0      1514341
            # 1      1495105
            # 2      1387438
            # 3      1345806
            # 4      1962417
            # ...        ...
            # 11995  1537932
            # 11996  1970199
            # 11997   650399
            # 11998  1551349
            # 11999   999198

            # [12000 rows x 1 columns]

print(df[['Salary']][8:22])
print()

            #      Salary
            # 8   1271285
            # 9    821755
            # 10  1621641
            # 11   624707
            # 12   855997
            # 13  1614164
            # 14  1119958
            # 15  1630198
            # 16   363332
            # 17  1352955
            # 18   971856
            # 19   613716
            # 20   984228
            # 21   305283

print(df[['Salary', 'Company']][8:22])
print()

            #    Salary     Company
            # 8   1271285      Amazon
            # 9    821755      Amazon
            # 10  1621641     Infosys
            # 11   624707       Wipro
            # 12   855997         TCS
            # 13  1614164      Google
            # 14  1119958      Amazon
            # 15  1630198      Google
            # 16   363332  Microsoft
            # 17  1352955       Wipro
            # 18   971856     Infosys
            # 19   613716      Amazon
            # 20   984228    Deloitte
            # 21   305283         TCS

print(df[['Salary', 'Company']][8:22:2])
print()


            #      Salary     Company
            # 8   1271285      Amazon
            # 10  1621641     Infosys
            # 12   855997         TCS
            # 14  1119958      Amazon
            # 16   363332  Microsoft
            # 18   971856     Infosys
            # 20   984228    Deloitte

df['last_Year']= 2025
print(df)

            #       Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years  last_Year
            # 0                1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4       2025
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9       2025
            # 2                3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9       2025
            # 3                4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6       2025
            # 4                5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2       2025
            # ...            ...             ...        ...                 ...         ...        ...      ...               ...        ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0       2025
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9       2025
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8       2025
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0       2025
            # 11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5       2025

            # [12000 rows x 9 columns]

df.insert(loc=5,column='current_Year', value = 2026)
print(df)
print()

            #        Employee_ID            Name Department                Role     Company  current_Year       City   Salary  Experience_Years  last_Year
            # 0                1      Employee_1         IT   Backend Developer  Microsoft           2026     Mumbai  1514341               2.4       2025
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon          2026       Pune  1495105               8.9       2025
            # 2                3      Employee_3         IT  Frontend Developer         TCS          2026  Hyderabad  1387438              13.9       2025
            # 3                4      Employee_4         IT   Software Engineer  Microsoft           2026       Pune  1345806               0.6       2025
            # 4                5      Employee_5         IT      Data Scientist   Accenture          2026       Pune  1962417              10.2       2025
            # ...            ...             ...        ...                 ...         ...           ...        ...      ...               ...        ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft           2026      Delhi  1537932               1.0       2025
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte          2026      Delhi  1970199               6.9       2025
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS          2026  Hyderabad   650399               8.8       2025
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro          2026      Delhi  1551349               9.0       2025
            # 11999        12000  Employee_12000         IT             Auditor       Wipro          2026  Bangalore   999198               9.5       2025

            # [12000 rows x 10 columns]


# Categorical() --> this function gives how many categories are available in given data

categorical = pd.Categorical(df['Company'])
print(categorical)
print()
            # ['Microsoft ', 'Amazon', 'TCS', 'Microsoft ', 'Accenture', ..., 'Microsoft ', 'Deloitte', 'TCS', 'Wipro', 'Wipro']
            # Length: 12000
            # Categories (8, str): ['Accenture', 'Amazon', 'Deloitte', 'Google', 'Infosys', 'Microsoft ', 'TCS',Wipro']


#  Unique() --> this function gives how many unique data are available.

Unique_data = df['Salary'].unique()
print(Unique_data)
print()
            # [1514341 1495105 1387438 ...  650399 1551349  999198]

# Condition

Conditions_Statements =  df['Salary']>1000000
print(Conditions_Statements)
print()

            # 0         True
            # 1         True
            # 2         True
            # 3         True
            # 4         True
            #          ...
            # 11995     True
            # 11996     True
            # 11997    False
            # 11998     True
            # 11999    False
            # Name: Salary, Length: 12000, dtype: bool

Conditions_Statements_Info = df[df['Salary']>1000000]
print(Conditions_Statements_Info)
print()

#        Employee_ID            Name Department                Role     Company  current_Year       City   Salary  Experience_Years  last_Year
# 0                1      Employee_1         IT   Backend Developer  Microsoft           2026     Mumbai  1514341               2.4       2025
# 1                2      Employee_2    Finance     DevOps Engineer      Amazon          2026       Pune  1495105               8.9       2025
# 2                3      Employee_3         IT  Frontend Developer         TCS          2026  Hyderabad  1387438              13.9       2025
# 3                4      Employee_4         IT   Software Engineer  Microsoft           2026       Pune  1345806               0.6       2025
# 4                5      Employee_5         IT      Data Scientist   Accenture          2026       Pune  1962417              10.2       2025
# ...            ...             ...        ...                 ...         ...           ...        ...      ...               ...        ...
# 11990        11991  Employee_11991    Finance   Financial Analyst      Google          2026     Mumbai  1884604              11.1       2025
# 11991        11992  Employee_11992         IT        Risk Manager       Wipro          2026     Mumbai  1758479               8.4       2025
# 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft           2026      Delhi  1537932               1.0       2025
# 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte          2026      Delhi  1970199               6.9       2025
# 11998        11999  Employee_11999         IT      Data Scientist       Wipro          2026      Delhi  1551349               9.0       2025

# [7104 rows x 10 columns]


print(len(df[df['Salary']>1000000])) # 7104
print()


print(df.iloc[0:10,[1,4,5,6]])

            #           Name     Company  current_Year       City
            # 0   Employee_1  Microsoft           2026     Mumbai
            # 1   Employee_2      Amazon          2026       Pune
            # 2   Employee_3         TCS          2026  Hyderabad
            # 3   Employee_4  Microsoft           2026       Pune
            # 4   Employee_5   Accenture          2026       Pune
            # 5   Employee_6      Google          2026  Bangalore
            # 6   Employee_7      Google          2026     Mumbai
            # 7   Employee_8   Accenture          2026     Mumbai
            # 8   Employee_9      Amazon          2026       Pune
            # 9  Employee_10      Amazon          2026  Bangalore