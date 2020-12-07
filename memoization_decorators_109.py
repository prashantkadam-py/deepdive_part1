def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print("{0} Time taken by {1}".format(end - start, fn.__name__))
        return result
    return inner


class Fib:

    def __init__(self):
        self.cache = {1 : 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print("Calculating fib({0})".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)

        return self.cache[n]


def fib_closure():
    cache = { 1: 1, 2: 1 }
    
    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2)

        return cache[n]
    return calc_fib

def memoize_fib(fib):

    cache = {1: 1, 2:1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return inner

def memoize(fn):

    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner



from functools import lru_cache
#@memoize_fib
#@memoize
@lru_cache(maxsize = 10)
def fib(n):
    print("Calculating fib {0}".format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)



if __name__ == "__main__":
    print(fib(5))
    #fib(36)

    #obj = Fib()
    #obj.fib(35)
    #print(obj.fib(5))

    #fib_cl = fib_closure()
    #print(fib_cl(5))

