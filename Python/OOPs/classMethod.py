
class computer:


    brand = 'Abhay AI'

    @classmethod # class method is used to access class variables and methods without creating an object of the class
    def info(cls):
        return cls.brand


print(computer.info())


