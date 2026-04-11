num = int(input())

if num % 2 == 0:
    print('Even')
else:
    print('Odd')


match num:

    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")