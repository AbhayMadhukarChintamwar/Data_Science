class computer:
    def config(self):
        print("i7, 32GB, 1TB, 16GB VRAM")


comp1 = computer()
comp2 = computer()



# computer.config(comp1) # calling method using class name
# computer.config(comp2) # calling method using class name

comp1.config() # calling method using object name
comp2.config() # calling method using object name

