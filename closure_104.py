
def counter(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b

if __name__ == "__main__":
    
    counters = {}
    counter_add = counter(add, counters)
    counter_mult = counter(mult, counters)
    counter_add(10, 20)
    counter_add(30, 40)
    counter_mult(10, 20)
    counter_mult(30, 40)
    print(counters)







