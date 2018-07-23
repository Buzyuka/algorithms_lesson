# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

lst = input("Введите список через запятую: ")
lst = list(map(int, lst.split(",")))

negatives = filter(lambda x: x[1] < 0, enumerate(lst))
max_item = max(negatives, key=lambda x: x[1])

print(f"Максиальный среди отрицательных: {max_item[1]}, индекс: {max_item[0]}")
