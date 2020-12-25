from functools import reduce
list_1 = []

for i in range(100, 1001, 2):
    list_1.append(i)

umn = reduce(lambda x, y: x * y, list_1)
print(umn)

# Тут я извиняюсь переписал ваш код, немного изменив
# Все еще пытаюсь нагнать
