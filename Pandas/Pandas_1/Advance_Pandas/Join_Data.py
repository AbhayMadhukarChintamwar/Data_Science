import pandas as pd

#  Join Method

Data_1 = pd.DataFrame({'key1':[1,2,3,4,5],
                       'key2':[6,7,8,9,10],
                       'key3':[11,12,13,14,15]}, index= ['a','b','c','d','e'])

print(Data_1)

            #    key1  key2  key3
            # a     1     6    11
            # b     2     7    12
            # c     3     8    13
            # d     4     9    14
            # e     5    10    15


Data_2 = pd.DataFrame({'key11':[1,20,3,40,5],
                       'key22':[6,70,8,9,10],
                       'key33':[131,120,139,14,150]}, index= ['a','b','f','g','h'])

print(Data_2)

            #    key11  key22  key33
            # a      1      6    131
            # b     20     70    120
            # f      3      8    139
            # g     40      9     14
            # h      5     10    150

Data_Join = Data_1.join(Data_2)
print(Data_Join)  #By Default Left Join

            #    key1  key2  key3  key11  key22  key33
            # a     1     6    11    1.0    6.0  131.0
            # b     2     7    12   20.0   70.0  120.0
            # c     3     8    13    NaN    NaN    NaN
            # d     4     9    14    NaN    NaN    NaN
            # e     5    10    15    NaN    NaN    NaN

Right_Join = Data_1.join(Data_2,how='right')
print(Right_Join)
            #   key1  key2  key3  key11  key22  key33
            # a   1.0   6.0  11.0      1      6    131
            # b   2.0   7.0  12.0     20     70    120
            # f   NaN   NaN   NaN      3      8    139
            # g   NaN   NaN   NaN     40      9     14
            # h   NaN   NaN   NaN      5     10    150

Inner_Join = Data_1.join(Data_2, how='inner')
print(Inner_Join)

            #    key1  key2  key3  key11  key22  key33
            # a     1     6    11      1      6    131
            # b     2     7    12     20     70    120

Outer_Join = Data_1.join(Data_2, how='outer')
print(Outer_Join)

            #   key1  key2  key3  key11  key22  key33
            # a   1.0   6.0  11.0    1.0    6.0  131.0
            # b   2.0   7.0  12.0   20.0   70.0  120.0
            # c   3.0   8.0  13.0    NaN    NaN    NaN
            # d   4.0   9.0  14.0    NaN    NaN    NaN
            # e   5.0  10.0  15.0    NaN    NaN    NaN
            # f   NaN   NaN   NaN    3.0    8.0  139.0
            # g   NaN   NaN   NaN   40.0    9.0   14.0
            # h   NaN   NaN   NaN    5.0   10.0  150.0


Cross_Join = Data_1.join(Data_2, how='cross')
print(Cross_Join)

            #     key1  key2  key3  key11  key22  key33
            # 0      1     6    11      1      6    131
            # 1      1     6    11     20     70    120
            # 2      1     6    11      3      8    139
            # 3      1     6    11     40      9     14
            # 4      1     6    11      5     10    150
            # 5      2     7    12      1      6    131
            # 6      2     7    12     20     70    120
            # 7      2     7    12      3      8    139
            # 8      2     7    12     40      9     14
            # 9      2     7    12      5     10    150
            # 10     3     8    13      1      6    131
            # 11     3     8    13     20     70    120
            # 12     3     8    13      3      8    139
            # 13     3     8    13     40      9     14
            # 14     3     8    13      5     10    150
            # 15     4     9    14      1      6    131
            # 16     4     9    14     20     70    120
            # 17     4     9    14      3      8    139
            # 18     4     9    14     40      9     14
            # 19     4     9    14      5     10    150
            # 20     5    10    15      1      6    131
            # 21     5    10    15     20     70    120
            # 22     5    10    15      3      8    139
            # 23     5    10    15     40      9     14
            # 24     5    10    15      5     10    150