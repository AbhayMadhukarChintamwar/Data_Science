import matplotlib.pyplot as plt
import numpy as np

x = ['car', 'bike', 'scooty','bicycle']
y = [40, 85, 75, 35]
z = [20,30,40,15]
width = 0.2
p  = np.arange(len(x))
p1 = [j+ width for j in p]
# c = ['red','yellow','green','magenta']
plt.xlabel('Vehicles')
plt.ylabel('Numbers of Vehicles')
plt.title('Parking survey')
plt.xticks(p +width/2, x, rotation = 30)
plt.bar(p,y, color = 'r', edgecolor = 'b')
plt.bar(p1,z, color = 'g', edgecolor = 'b')

print(plt.show())