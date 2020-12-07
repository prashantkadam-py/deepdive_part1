from time import perf_counter
from time import sleep

class Averager(object):
    def __init__(self):
        self.total = 0
        self.count = 0

    def __call__(self, number):
        self.total += number
        self.count += 1
        print(self.total/self.count)
        return self.total/self.count



class Timer(object):
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start





def averager():

    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        print(total/count)
        return total/count
    return add


def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


if __name__ == "__main__":
    obj = Averager()
    obj(10)
    obj(20)
    obj(30)

    obj = Timer()
    print(obj())
    sleep(5)
    print(obj())
    sleep(5)
    print(obj())
    sleep(5)
    
    avg = averager()
    avg(10)
    avg(20)
    avg(30)

    timeit = timer()
    print(timeit())
    sleep(5)
    print(timeit())
    sleep(5)
    print(timeit())
    sleep(5)

        
