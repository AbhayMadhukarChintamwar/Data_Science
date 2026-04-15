
def person(name, **kwlargs):
    print("Name :", name)
    # print(kwlargs)
    for k, v in kwlargs.items():
        print(k," : ", v)

# person(age = 24, name = "Abhay")  # keyword arguments, the order of arguments does not matter when calling the function with keyword arguments
person( name = "Abhay", age=24,loc ="Hyderabad",tech = "Python")  # keyword arguments with additional arguments, the function will ignore the additional arguments that are not defined in the function


# def add(num1, num2):     # define a function named add that takes two parameters num1 and num2
#     return num1 + num2


# def add(num1, *num2):   # variable length arguments, num2 can take any number of arguments
#     total = num1  # initialize total with the value of num1
#     for n in num2:  # iterate over each number in num2
#         total += n  # add each number to total
#     return total  # return the final total

# result = add(10, 20, 30, 40)  # call the add function with multiple arguments
# print(result)  # print the result
