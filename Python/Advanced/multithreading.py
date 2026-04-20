
from threading import Thread
from time import sleep



def Hello():
    for i in range(5):
        print('Hello ', i+1)
        sleep(.3)


def Hi():
    for i in range(5):
        print('Hi ', i+1)
        sleep(.3)



if __name__ == '__main__':

    t1 = Thread(target=Hello)
    t2 = Thread(target=Hi)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Bye')