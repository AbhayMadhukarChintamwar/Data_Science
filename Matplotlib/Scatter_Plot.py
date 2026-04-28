import matplotlib.pyplot as plt

# Scatter Plot

x = [1,2,3,4,5,6]
y = [4,2,3,5,1,8]
plt.title('Scatter Plot', fontsize = 20)
plt.xlabel('Month')
plt.ylabel('Number')
# plt.scatter(x,y, color ='r')
size = [300,170, 350, 264, 209, 219]
c = [10,20,30,45,78,99]
plt.scatter(x,y, c = c , s=size , cmap ='Accent')
plt.show()