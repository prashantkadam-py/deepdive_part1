

class MyDecorator(object):

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __call__(self, fn):

        def inner(*args, **kwargs):
            print(f"decoration function {fn.__name__} called: a ={self.a} b = {self.b}")
            return fn(*args, **kwargs)

        return inner


@MyDecorator(10, 20)
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(30, 40))

