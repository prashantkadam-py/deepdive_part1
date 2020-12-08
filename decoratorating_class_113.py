def debug_info(cls):
    def inner(self):
        results = []
        results.append(f"class : {self.__class__.__name__}")
        results.append(f"id : {hex(id(self))}")

        for k, v in vars(self).items():
            results.append(f"{k} : {v}")
        return results

        
    cls.debug = inner
    return cls

@debug_info
class Automobile(object):

    def __init__(self, make, model, year, top_speed):

        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError(f"Speed cannot be greater than top speed = {self.top_speed}")

        else:
            self._speed = new_speed



if __name__ == "__main__":
    obj = Automobile("Honda", "Activa 4G", "2017", 120)
    print(obj.debug())
