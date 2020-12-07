def timed(fn):

    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()   
        
        result = fn(*args, **kwargs)
        
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ["{0}={1}".format(k, v) for (k,v) in kwargs.items()]

        all_args = args_ + kwargs_
        args_str = ", ".join(all_args)

        print("{0}({1}) took {2:.6f}s to run.".format(fn.__name__, 
                                                      args_str, 
                                                      elapsed))
        return result

    return inner






def calc_fib_recursive(n, val = ""):
    if n <= 2:
        #print("n< ", n, val)
        return 1

    else:
        #print("n> ", n, val)
        result = calc_fib_recursive(n-1, 1) + calc_fib_recursive(n-2, 2)
        #print("result : ", result)
        return result

@timed
def fib_recursive(n):
    return calc_fib_recursive(n)



@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(3, n+1):
        #print("iteration ", i)
        #print(fib_1, fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)

    dummy = range(n)

    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                            dummy, initial)
    return fib_n


if __name__ == "__main__":

    #fib_recursive(4)
    #import pdb;pdb.set_trace()
    print(fib_recursive(10))
    fib_recursive(35)
    fib_recursive(36)
    fib_recursive(37)

    print(fib_loop(10))
    fib_loop(35)
    fib_loop(36)
    fib_loop(37)

    
    print(fib_reduce(10))
    fib_reduce(35)
    fib_reduce(36)
    fib_reduce(37)





