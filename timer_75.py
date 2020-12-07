import time


def compute_powers_1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n ** i)
    return results


def compute_powers_2(n, *, start=1, end):
    return [n ** i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    return (n ** i for i in range(start, end))



def time_it(fn, *args, rep = 1, **kwargs):
    print("args ------>", args)
    print("kwargs ----->", kwargs)
    start = time.perf_counter()
    
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep




if __name__ == "__main__":
    print(time_it(compute_powers_1, 2, start=0, end=20000, rep=5))
    print(time_it(compute_powers_1, n = 2, start=0, rep=5, end=20000))
    print(time_it(compute_powers_2, n = 2, start=0, rep=5, end=20000))
    print(time_it(compute_powers_3, n = 2, start=0, rep=5, end=20000))


    

