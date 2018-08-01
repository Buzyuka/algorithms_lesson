# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from memtool import *


def vars(names):
    return [(name.strip(), eval(name)) for name in names.split(",")]


matrix = []
min_values = []

for _ in range(0, 4):
    row = input("Введите 4 элемента строки: ")
    row = list(map(int, row.split(",")))
    matrix.append(row)


for idx in range(0, len(matrix)):
    column = map(lambda x: x[idx], matrix)
    min_values.append(min(column))


max_ = max(min_values)

mem_trace(*vars("matrix, min_values, max_"))
print_mem_analyze()
