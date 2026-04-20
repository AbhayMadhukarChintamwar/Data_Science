
class Laptop:  # duck
    def build(self):
        print('Building a laptop')

class Desktop: # crow
    def build(self):
        print('Building a desktop')

class Tablet: # duck typing - if it looks like a duck and quacks like a duck, then it is a duck
    def open_pdf(self):
        print('Opening a PDF on the tablet')


class Alien:
    def code(self, machine : Laptop):
        machine.build()

mac = Laptop()
dell= Desktop()
samsung = Tablet()

abhay = Alien()

abhay.code(mac)
abhay.code(dell)

# abhay.code(samsung) # this will raise an error because samsung does not have a build method
