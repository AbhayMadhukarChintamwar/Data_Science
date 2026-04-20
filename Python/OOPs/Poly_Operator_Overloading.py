
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self): # operator overloading for string representation of the object
        return f'{self.name} : {self.balance}'

    def __add__(self, other): # operator overloading for addition of two objects
        return Account('combined', self.balance + other.balance)


user1 = Account('User1', 1000)
user2 = Account('User2', 1000)

combined = user1 + user2

print(user1)
print(user2)
print(combined)