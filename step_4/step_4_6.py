from random import randint
from itertools import count, cycle


def rand(x, y):
    i = 0
    while True:
        i += 1
        if i > 25:
            break
        yield randint(x, y)


def rand_2(x):
    for el1 in count(x):
        yield el1
        if el1 == 500:
            break


def iter_list(one):
    i = 0
    for el in cycle(one):
        i += 1
        print(el)
        if i > 50:
            break



for el2 in rand_2(15):
    print(el2)
# Я возможно просто не понял задание поэтому написал оба варианта

for el in rand(10, 1000000000000000000000000000000000000000):
    print(el)

list_new = [1, 4567, 'qwe1', 50505]
iter_list(list_new)