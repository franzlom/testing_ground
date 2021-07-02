class Abc():

    def __init__(self):
        self.abc = 123

    def something(self):
        self.abc = self.abc + 321


if __name__ == '__main__':
    print('hello')
    cxz = Abc()

    print(cxz.abc)
    cxz.something()
    print(cxz.abc)
