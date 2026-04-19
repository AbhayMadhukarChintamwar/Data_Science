
def log_deco(func):
    def wrap(*args):
        print('values ', args)
        result = func(*args)
        print('result ', result)
        return result
    return wrap

def greater_first(func): #decorator
    def wrap(a,b):
        if a<b:
            a,b = b,a #swap the values of a and b if a is less than b
        return func(a,b) #call the original function
    return wrap  #return the wrapper function

@log_deco #decorator
@greater_first #decorator
def divide(a,b):
    return a/b


@greater_first #decorator
def subtract(a,b):
    return a-b

@log_deco #decorator
def add(a,b,c):
    return a+b+c

result1 = divide(4,7)
print(result1)

result2 = subtract(4,2)
print(result2)

result3 = add(4,2,6)
print(result3)
