# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

lst = input("Введите список через запятую: ")
lst = list(map(int, lst.split(",")))

first_min_item = min(lst)
lst.remove(first_min_item)
second_min_item = min(lst)

print(f"{first_min_item}, {second_min_item}")
