from math import factorial


def fact(one):
    for el in range(1, one + 1):
        factor = factorial(el)
        print(factor)
    yield factor


n = 20
print(fact(n))
for step in fact(n):
    #  print(fact(n))
    print(f'{step} - факториал {n}')  #


