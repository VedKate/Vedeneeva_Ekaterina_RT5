from random import randint


def gen_random(n: int, st: int, fin: int):
    l: list = []
    for i in range(n):
        l.append(randint(st, fin))
    return l
