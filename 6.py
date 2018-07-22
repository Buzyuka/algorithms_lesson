# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

import random
from functools import reduce

n = 10

lst = list(map(lambda _: random.randint(0, n), range(0, n)))
print(lst)

enumerated = list(enumerate(lst))

max_item = max(enumerated, key=lambda x: x[1])
min_item = min(enumerated, key=lambda x: x[1])


def predicate(x):
    return min_item[0] < x[0] < max_item[0] or \
           min_item[0] > x[0] > max_item[0]


filtered = filter(predicate, enumerated)
range_sum = reduce(lambda a, b: a + b[1], filtered, 0)

print(range_sum)
