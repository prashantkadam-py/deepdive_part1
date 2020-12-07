
def timed(reps):

    def dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                elapsed = end - start
                total_elapsed += elapsed
            
            print("Avg run time is {0:.6f}s {1} reps".format((total_elapsed/reps), reps))
            return result
        return inner
    return dec



def calc_fib_rec(n):
    
    return 1 if n < 3 else calc_fib_rec(n-2) + calc_fib_rec(n-1)



@timed(100)
def fib(n):
   return calc_fib_rec(n)

if __name__ == "__main__":
    fib(12)

