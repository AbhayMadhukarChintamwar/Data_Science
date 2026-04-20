
class computer:

    @staticmethod # static method is used to access class variables and methods without creating an object of the class
    def gb_to_byte(gb):
        return gb * (1024 ** 3)


print(computer.gb_to_byte(16)) # calling static method using class name


