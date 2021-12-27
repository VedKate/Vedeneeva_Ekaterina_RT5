from process_data import *
from sort import *
from printer import *
from cm_timer import *
from feild import *
from gen_random import *
from unique import *


def ex1():
    goods = [
        {'title': 'Ковер', 'price': 15000, 'color': 'синий'},
        {'title': 'Диван для отдыха', 'color': 'зеленый'},
        {'color': 'Рыжий'},
        {'color': 'желтый'},
        {'title': None, 'price': 25, 'color': 'красный'}
    ]
    print('Задание 1')
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))


def ex2():
    print('\n\nЗадание 2')
    print(gen_random(5, 1, 3))


def ex3():
    print('\n\nЗадание 3')
    print('Обработка разного списка')
    data = [1, 1, 1, 1, 1, 2, 2, 2, '2', 2, 2, 'F', 'f', 'A']
    mycl = Unique(data, ignore_case=True)
    myit = iter(mycl)
    while True:
        try:
            print(next(myit))
        except StopIteration:
            break

    print('Обработка генератора')
    mycl1 = Unique(gen_random(10, 1, 3))
    myit1 = iter(mycl1)
    while True:
        try:
            print(next(myit1))
        except StopIteration:
            break


def ex4():
    print('\n\nЗадание 4')
    data = [4, -15, 15, 200, -200, 123, 3, 0, -3, -4]
    srt(data)


def ex5():
    print('\n\nЗадание 5')
    all_test()


def ex6():
    print('\n\nЗадание 6')
    test_cm_timer()


def ex7():
    print('\n\nЗадание 7')
    start()


def main():
    a = (ex1, ex2, ex3, ex4, ex5, ex6, ex7)
    while True:
        print('Выберите задание 1-7:')
        i = int(input())
        if i != 0:
            a[i-1]()
        else:
            return


if __name__ == '__main__':
    main()
