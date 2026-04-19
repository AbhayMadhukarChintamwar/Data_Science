
def greater_first(func): #decorator
    def wrap(a,b):
        if a<b:
            a,b = b,a #swap the values of a and b if a is less than b
        return func(a,b) #call the original function
    return wrap  #return the wrapper function

# @greater_first #decorator
def divide(a,b):
    return a/b

# @greater_first #decorator
def subtract(a,b):
    return a-b


divide = greater_first(divide) #we can also use the decorator by calling the greater_first function and passing the divide function as an argument. This will return the wrapper function which we can assign to the divide variable.
subtract = greater_first(subtract) #we can also use the decorator by calling the greater_first function and passing the subtract function as an argument. This will return the wrapper function which we can assign to the subtract variable.

result1 = divide(4,2)
print(result1)

result2 = subtract(4,2)
print(result2)
