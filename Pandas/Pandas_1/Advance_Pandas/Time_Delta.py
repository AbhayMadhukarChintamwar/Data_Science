import pandas as pd

TimeDelta = pd.Timedelta(days = 1, hours = 5, minutes = 45)
print(TimeDelta)
print()
            # 1 days 05:45:00

dt = pd.to_datetime('2002-03-08')
td = pd.Timedelta(days =3)

print(dt + td)
print()
            # 2002-03-11 00:00:00

m1 = pd.Timedelta(days = 1, hours = 5, minutes = 45)
m2 = pd.Timedelta(days = 5, hours = 15, minutes = 55)

difference = m2-m1
print(difference)
            # 4 days 10:10:00

