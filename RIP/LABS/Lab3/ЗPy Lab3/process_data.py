import json
from random import randint
from printer import print_result
from cm_timer import cm_timer_1


def start():
    with open('data_light.json', 'r',
              encoding='utf-8') as f:  # открываем файл personal.json и указываем его кодировку — что бы можно было работать с русскими буквами
        data = json.load(f)  # загоняем в переменную все, что получилось в результате работы библиотеки
        print(type(f1(data)))
        with cm_timer_1():
            f4(f3(f2(f1(data))))


@print_result
def f1(arg):
    return set([x.get("job-name") for x in arg])

@print_result
def f2(arg):
    return list(filter((lambda x: x.split()[0].lower() in 'программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    return list(zip(arg, list(map(lambda x: 'с зарплатой ' + x + ' рублей', [str(randint(100000, 200000)) for x in range(len(arg))]))))

