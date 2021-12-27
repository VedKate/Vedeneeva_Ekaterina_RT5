def print_result(func):
    def wrapper(*arg):
        print('\nИмя функции: {}'.format(func.__name__))
        print('Результат:')
        a = func(*arg)
        if type(a) in (list, map, zip, tuple, set):
            print(*a, sep='\n')
        elif type(a) == dict:
            for key, value in a.items():
                print("{} = {}".format(key, value))
        else:
            print(a)
        
        return a

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2, 'c': 3, 'd': 4}


@print_result
def test_4():
    return [1, 2, 'a', 28]


def all_test():
    test_1()
    test_2()
    test_3()
    test_4()

