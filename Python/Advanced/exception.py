
# a = 5
# b = 0   # ZeroDivisionError: division by zero

try:

    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    result = a / b
    print(result)

except Exception as e:
    print("An error occurred : ",e)

print('End of the execution')


