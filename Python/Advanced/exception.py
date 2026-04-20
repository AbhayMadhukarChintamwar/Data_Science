
a = 5
b = 0    # ZeroDivisionError: division by zero

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print('End of the execution')


