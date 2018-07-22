# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

from pprint import pprint

matrix = []

for _ in range(0, 4):
    row = input("Введите 4 элемента строки: ")
    row = list(map(int, row.split(",")))
    row.append(sum(row))
    matrix.append(row)

pprint(matrix, width=20)
