
class computer:


    def __init__(self, cpu, ram, hdd, vram, gpu): # constructor method
        print('init method called') # this method will be called automatically when we create an object of the class
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.vram = vram
        self.gpu = gpu


    def config(self):
        print('config :', self.cpu, self.ram, self.hdd, self.vram, self.gpu) # this method will print the configuration of the computer


comp1 = computer('i5', '16GB', '512GB', '8GB VRAM', 'NVIDIA GTX 4050') # creating an object of the class computer and passing the configuration as arguments
comp2 = computer('i9', '64GB', '2TB', '32GB VRAM', 'NVIDIA RTX 4090') # creating another object of the class computer and passing the configuration as arguments


comp1.config() # calling method using object name
comp2.config() # calling method using object name


