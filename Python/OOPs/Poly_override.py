
class A:

    def show(self):
        print('in A show')

class B(A):

    def show(self):
        print('in B show')

obj = B()
obj.show() # it will call the show method of class B because it is overriding the show