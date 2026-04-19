def log(fun):
    def wrap(*args):
        print('values ', args)
        result = fun(*args)
        print('result ', result)
        return result
    return wrap

def  greater_first(fun):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return wrap

@log
@greater_first
def add(a,b):
    return a +b

@log
@greater_first
def sub(a,b):
    return a - b


if __name__ == '__main__':
    print('in calc',add(6,5))
    print('in calc',sub(7,5))