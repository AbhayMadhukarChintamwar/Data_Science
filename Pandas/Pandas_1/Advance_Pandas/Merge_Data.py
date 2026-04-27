import pandas as pd


#  Merge --> Merging data

Data_1 = pd.DataFrame({'key1':[1,2,3,4,5],
              'key2':[6,7,8,9,10],
             'key3':[11,12,13,14,15]})

print(Data_1)

            #    key1  key2  key3
            # 0     1     6    11
            # 1     2     7    12
            # 2     3     8    13
            # 3     4     9    14
            # 4     5    10    15

Data_2 = pd.DataFrame({'key1':[1,20,3,40,5],
              'key4':[6,70,8,9,10],
             'key5':[131,120,139,14,150]})

print(Data_2)

            #    key1  key4  key5
            # 0     1     6   131
            # 1    20    70   120
            # 2     3     8   139
            # 3    40     9    14
            # 4     5    10   150

Merge_Data = pd.merge(Data_1,Data_2)
print(Merge_Data) # By default its print inner merge values

            #    key1  key2  key3  key4  key5
            # 0     1     6    11     6   131
            # 1     3     8    13     8   139
            # 2     5    10    15    10   150

Left_Merge = pd.merge(Data_1, Data_2, how='left')
print(Left_Merge)

            #    key1  key2  key3  key4   key5
            # 0     1     6    11   6.0  131.0
            # 1     2     7    12   NaN    NaN
            # 2     3     8    13   8.0  139.0
            # 3     4     9    14   NaN    NaN
            # 4     5    10    15  10.0  150.0


Right_Merge = pd.merge(Data_1, Data_2, how='right')
print(Right_Merge)
            #    key1  key2  key3  key4  key5
            # 0     1   6.0  11.0     6   131
            # 1    20   NaN   NaN    70   120
            # 2     3   8.0  13.0     8   139
            # 3    40   NaN   NaN     9    14
            # 4     5  10.0  15.0    10   150

Outer_Merge = pd.merge(Data_1, Data_2, how='outer')
print(Outer_Merge)

            #   key1  key2  key3  key4   key5
            # 0     1   6.0  11.0   6.0  131.0
            # 1     2   7.0  12.0   NaN    NaN
            # 2     3   8.0  13.0   8.0  139.0
            # 3     4   9.0  14.0   NaN    NaN
            # 4     5  10.0  15.0  10.0  150.0
            # 5    20   NaN   NaN  70.0  120.0
            # 6    40   NaN   NaN   9.0   14.0

Cross_Merge = pd.merge(Data_1,Data_2, how='cross')
print(Cross_Merge)

            #   key1_x  key2  key3  key1_y  key4  key5
            # 0        1     6    11       1     6   131
            # 1        1     6    11      20    70   120
            # 2        1     6    11       3     8   139
            # 3        1     6    11      40     9    14
            # 4        1     6    11       5    10   150
            # 5        2     7    12       1     6   131
            # 6        2     7    12      20    70   120
            # 7        2     7    12       3     8   139
            # 8        2     7    12      40     9    14
            # 9        2     7    12       5    10   150
            # 10       3     8    13       1     6   131
            # 11       3     8    13      20    70   120
            # 12       3     8    13       3     8   139
            # 13       3     8    13      40     9    14
            # 14       3     8    13       5    10   150
            # 15       4     9    14       1     6   131
            # 16       4     9    14      20    70   120
            # 17       4     9    14       3     8   139
            # 18       4     9    14      40     9    14
            # 19       4     9    14       5    10   150
            # 20       5    10    15       1     6   131
            # 21       5    10    15      20    70   120
            # 22       5    10    15       3     8   139
            # 23       5    10    15      40     9    14
            # 24       5    10    15       5    10   150

