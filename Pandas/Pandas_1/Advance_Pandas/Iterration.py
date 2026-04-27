import pandas as pd

data = {'a' :[1,2,3],
        'b':[4,5,6],
        'c':['Rose','Lotus','Lily']
}

df = pd.DataFrame(data)
print(df)

            #    a  b      c
            # 0  1  4   Rose
            # 1  2  5  Lotus
            # 2  3  6   Lily

Change_Indexing = pd.DataFrame(data, index = ['a1','b1','c1'])
print(Change_Indexing)

            #     a  b      c
            # a1  1  4   Rose
            # b1  2  5  Lotus
            # c1  3  6   Lily

Re_Indexing = Change_Indexing.reindex(['c1','a1','b1'])
print(Re_Indexing)

            #     a  b      c
            # c1  3  6   Lily
            # a1  1  4   Rose
            # b1  2  5  Lotus

Iter_Data  = df.iterrows()
print(Iter_Data)
            # <generator object DataFrame.iterrows at 0x000001EAAD320040>


for i in Change_Indexing.iterrows():
    print(i)

print()

            # ('a1', a       1
            # b       4
            # c    Rose
            # Name: a1, dtype: object)
            # ('b1', a        2
            # b        5
            # c    Lotus
            # Name: b1, dtype: object)
            # ('c1', a       3
            # b       6
            # c    Lily
            # Name: c1, dtype: object)


for i, j in Change_Indexing.iterrows():
    print(i,j)

print()

# a1 a       1
# b       4
# c    Rose
# Name: a1, dtype: object
# b1 a        2
# b        5
# c    Lotus
# Name: b1, dtype: object
# c1 a       3
# b       6
# c    Lily
# Name: c1, dtype: object


for i in Change_Indexing.itertuples():
    print(i)

print()

# Pandas(Index='a1', a=1, b=4, c='Rose')
# Pandas(Index='b1', a=2, b=5, c='Lotus')
# Pandas(Index='c1', a=3, b=6, c='Lily')