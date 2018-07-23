# Определить, какое число в массиве встречается чаще всего.

lst = input("Введите список через запятую: ")
lst = list(map(int, lst.split(",")))

count_lst = map(lambda x: lst.count(x), lst)
list_with_count = zip(lst, count_lst)
max_count = max(list_with_count, key=lambda x: x[1])

print(max_count[0])
