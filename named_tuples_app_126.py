from collections import namedtuple

Color = namedtuple("Color", "red green blue alpha")

def random_color():
    red, green, blue, alpha = 1, 2, 3, 4
    return Color(red, green, blue, alpha)



def tuplify_dicts(dicts):

    keys = { key for dict_ in dicts for key in dict_ }
    Struct = namedtuple("Struct", sorted(keys), rename = True)
    Struct.__new__.__defaults__  = (None, ) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]


if __name__ == "__main__":
    r,g,b,a = random_color()
    print(r,g,b,a)

    dicts = [
             {"key1" : 100, "key2" : 200},
             {"key2" : 400, "key3" : 600},
             {"key1" : 300, "key3" : 1200}
            ]
    print(tuplify_dicts(dicts))
