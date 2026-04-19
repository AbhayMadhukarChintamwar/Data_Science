def square(num):
    return num * num

def cube(num):
    return num * num * num



def operate(num, operation): # this is a higher order function because it takes another function as an argument
    return operation(num)    # this will call the operation function with num as an argument and return the result


value = 5
result = operate(value,square)
result1 = operate(value,cube)
print(result)  # This will print 25
print(result1)    # This will print 125