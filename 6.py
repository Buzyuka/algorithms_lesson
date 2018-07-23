# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

from functools import reduce

lst = input("Введите список через запятую: ")
lst = map(int, lst.split(","))

enumerated = list(enumerate(lst))

max_item = max(enumerated, key=lambda x: x[1])
min_item = min(enumerated, key=lambda x: x[1])


def predicate(x):
    return min_item[0] < x[0] < max_item[0] or \
           min_item[0] > x[0] > max_item[0]


filtered = filter(predicate, enumerated)
range_sum = reduce(lambda a, b: a + b[1], filtered, 0)

print(range_sum)
