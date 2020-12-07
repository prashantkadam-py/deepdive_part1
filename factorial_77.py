

def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f"calculating {n}!")
        result = n * factorial(n-1)
        cache[n] = result
        return result


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(5))
