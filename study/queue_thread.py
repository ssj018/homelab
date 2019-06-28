from threading import Thread
from queue import Queue
import random
import time


class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.data = queue

    def run(self):
        for i in range(20):
            random_num = random.randint(1, 100)
            # print(random_num)
            self.data.put(random_num)
            time.sleep(1)
        print('{}: Producer is finished'.format(time.ctime()))


class ConsumerEven(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.data = queue

    def run(self):
        while 1:
            try:
                val_even = self.data.get(True, 5)
                if val_even % 2 == 0:
                    print("{} even is consuming... {} is consumed!".format(time.ctime(),val_even))
                    time.sleep(2)
                else:
                    self.data.put(val_even)
            except:
                print("{} even is finished".format(time.ctime()))
                break


class ConsumerOdd(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.data = queue

    def run(self):
        while 1:
            try:
                val_odd = self.data.get(True, 5)
                if val_odd % 2 != 0:
                    print("{} odd is consuming... {} is consumed!".format(time.ctime(), val_odd))
                    time.sleep(2)
                else:
                    self.data.put(val_odd)
                    time.sleep(2)
            except:
                print("{} odd is finished".format(time.ctime()))
                break


if __name__ == '__main__':
     queue = Queue()
     producer = Producer(queue)
     cusumer_even = ConsumerEven(queue)
     cusumer_odd = ConsumerOdd(queue)

     producer.start()
     cusumer_even.start()
     cusumer_odd.start()

     producer.join()
     cusumer_even.join()
     cusumer_odd.join()

     print("done")