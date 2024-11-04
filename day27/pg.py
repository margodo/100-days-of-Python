# # unlimited arguments
# def add(*args):
#     suma = 0
#     for n in args:
#         suma += n
#     return suma
# print(add(1,5,6,1))

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # for key, value in kwargs.items():
    #     return kwargs[key]
    return n

print(calculate(2,add = 3, multiply = 5))
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make ="nissan")
print(my_car.model)