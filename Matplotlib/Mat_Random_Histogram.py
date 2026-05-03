import matplotlib.pyplot as plt
import numpy as np

random_number = np.random.randint(1,100 , (50))
# l = [0,10, 20, 30, 40, 50, 60, 70, 80, 90,100]
new_histogram = random_number
plt.hist(new_histogram,'auto',(0,150), color = 'r' , edgecolor = 'b')
plt.title('Random Histogram')
plt.xlabel('Python')
plt.ylabel('Java')
plt.show()