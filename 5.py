# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

n = 10

lst = list(map(lambda _: random.randint(-n, n), range(0, n)))
print(lst)

enumerated = enumerate(lst)
negatives = filter(lambda x: x[1] < 0, enumerated)
max_item = max(negatives, key=lambda x: x[1])

print(f"Максиальный среди отрицательных: {max_item[1]}, индекс: {max_item[0]}")
