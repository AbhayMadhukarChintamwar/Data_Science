

from threading import Thread
from time import sleep

class MyThread(Thread):

    def run(self):
        for i in range(5):
            print('Hello ', i+1)
            sleep(.3)


class MyThread2(Thread):

    def run(self):
        for i in range(5):
            print('Hi ', i+1)
            sleep(.3)



if __name__ == '__main__':

    t1 = MyThread()
    t2 = MyThread2()

    t1.start()
    t2.start()