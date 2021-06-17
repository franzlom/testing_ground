# testing looping

def test1(input):
    print('________trying to write over value in list through loop________')
    for x in some_list:
        print(x)
        x = 2
    print(some_list)

    print('________with enumerate________')

    for k, v in enumerate(some_list):
        print(v)
        some_list[k] = 2

    print(some_list)


def test2(input):

    for k,v in enumerate(input):
        print(f'v = {v}')
        yield [int(s) for s in v.split() if s.isdigit()]


if __name__ == '__main__':
    some_list = [123, 321, 231]
    some_list2 = 'uptime is 8 weeks, 1 day, 21 hours, 4 minutes'

    # test1 = test1(some_list)

    a = test2(some_list)
    print(list(a))
