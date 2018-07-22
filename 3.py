# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

n = 10

lst = list(map(lambda _: random.randint(0, n), range(0, n)))
print(lst)

idx = range(0, n)
enumerated = list(zip(idx, lst))

max_item = max(enumerated, key=lambda x: x[1])
min_item = min(enumerated, key=lambda x: x[1])

lst[max_item[0]] = min_item[1]
lst[min_item[0]] = max_item[1]

print(lst)
