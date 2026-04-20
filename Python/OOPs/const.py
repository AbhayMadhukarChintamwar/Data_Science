
class Abc:

    def __new__(cls):  # this method is called when we create an object of the class and it is used to create an instance of the class
        print('Constructor called')
        return super(Abc, cls).__new__(cls)

    def __init__(self):
        print("init called")

    def show(self):
        print("in show")

obj1 = Abc() # creating an object of the class Abc and calling the constructor method
obj1.show() # calling the method using the object created by calling the constructor method

obj2 = Abc.__new__(Abc) # creating an object without calling the constructor method
obj2.__init__() # manually calling the initializer method
obj2.show() # calling the method using the object created without calling the constructor method

