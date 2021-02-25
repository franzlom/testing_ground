# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Car:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f'the color of this car is {self.color}'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('before hi')
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    new_car = Car('red')
    print(new_car.color)


def test_id(obj):
    old_car = Car('Rusty Red')
    new_car = Car('Beautiful Blue')
    print(f'id of type = {type(id)}')
    print(f'id of {obj}, is {id(obj)}')
    print(f'id of {old_car}, is {id(old_car)}')
    print(f'id of {new_car}, is {id(new_car)}')


def print_val_in_list(x):
    print(x)


def meta_programming_magic():
    new_car = Car('benevolent blue')
    Car.magic_new_field = 'WHAT IS THIS MAGIC NEW FIELD CREATED WITHOUT BEING DEFINED'
    Car.method = lambda self: print('MAGIC METHOD FROM NOWHERE')

    print(new_car.magic_new_field)
    new_car.method()
    print(new_car)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test_id(12)
    meta_programming_magic()
