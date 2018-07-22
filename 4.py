# Определить, какое число в массиве встречается чаще всего.

import random

n = 10

lst = list(map(lambda _: random.randint(0, n), range(0, n)))
print(lst)

count_lst = map(lambda x: lst.count(x), lst)
enumerated = zip(lst, count_lst)
max_count = max(enumerated, key=lambda x: x[1])

print(max_count[0])
