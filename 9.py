# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = []
min_values = []

for _ in range(0, 4):
    row = input("Введите 4 элемента строки: ")
    row = list(map(int, row.split(",")))
    matrix.append(row)


for idx in range(0, len(matrix)):
    column = map(lambda x: x[idx], matrix)
    min_values.append(min(column))


print(max(min_values))
