# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from memtool import *


def vars(names):
    return [(name.strip(), eval(name)) for name in names.split(",")]


lst = input("Введите список через запятую: ")
lst = list(enumerate(map(int, lst.split(","))))

negatives = list(filter(lambda x: x[1] < 0, lst))
max_item = max(negatives, key=lambda x: x[1])

print(f"Максиальный среди отрицательных: {max_item[1]}, индекс: {max_item[0]}")

mem_trace(*vars("lst, negatives, max_item"))
print_mem_analyze()
