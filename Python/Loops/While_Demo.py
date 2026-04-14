# n = int(input())
n = 10
while n > 0:
    print(n, end=' ')
    n-=1

print()

data = [1,'Abhay',99.9,True,[1,2,3],(4,5,6),{'name':'Abhay','age':30}]
for item in data:
    print(item, end=' ')