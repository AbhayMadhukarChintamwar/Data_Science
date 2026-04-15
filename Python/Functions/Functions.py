


# def add(num1, num2):     # define a function named add that takes two parameters num1 and num2
#     return num1 + num2


def add(num1, *num2):   # variable length arguments, num2 can take any number of arguments
    total = num1  # initialize total with the value of num1
    for n in num2:  # iterate over each number in num2
        total += n  # add each number to total
    return total  # return the final total

result = add(10, 20, 30, 40)  # call the add function with multiple arguments
print(result)  # print the result 
