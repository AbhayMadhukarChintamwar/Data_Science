import matplotlib.pyplot as plt

# Scatter Plot

x = [1,2,3,4,5,6]
y = [4,2,3,5,1,8]
plt.title('Scatter Plot', fontsize = 20)
plt.xlabel('Month')
plt.ylabel('Number')
# plt.scatter(x,y, color ='r')
c = ['red','pink','yellow','blue','green','purple']
plt.scatter(x,y, color =c)

print(plt.show())