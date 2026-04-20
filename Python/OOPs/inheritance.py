
class A: # single inheritance

    def __init__(self):
        print('in A init')

    def f1(self):
        print('F1 works')

    def f2(self):
        print('F2 works')


class B(A): # single inheritance

    def __init__(self):
        super().__init__() # calling parent class constructor
        print('in B init')

    def f3(self):
        print('F3 works')

    def f4(self):
        print('F4 works')

class C(B):  # multiple inheritance

    def f5(self):
        print('F5 works')




obj = C()
obj.f1()
obj.f3()
obj.f5()