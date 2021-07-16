"""
what is yield and what does it do in python?

"""


def run(x):
    if isinstance(x, list):
        for i in x:
            yield i


if __name__ == '__main__':
    print('initializing...')
    lst = [123, 321, 213]
    output = run(lst)
    for x in output:
        print (x)