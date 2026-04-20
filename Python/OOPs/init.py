
class computer:


    def __init__(self): # constructor method
        print('init method called') # this method will be called automatically when we create an object of the class
        self.cpu = 'i7'


    def config(self):
        print("i7, 32GB, 1TB, 16GB VRAM, NVIDIA RTX 4060")


comp1 = computer()
comp2 = computer()

print(comp1.cpu) # accessing instance variable using object name

comp1.config() # calling method using object name
comp2.config() # calling method using object name


