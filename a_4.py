# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;

import random
import string

input_data = input("Введите границы для целого числа через .. (ex: 1..5): ")
a, b = tuple(map(int, input_data.split("..")))
b += 1  # включительно последнее число
print(random.randint(a, b))

# случайное вещественное число;
input_data = input("Введите границы для вещественного числа через .. (ex: 1..5): ")
a, b = tuple(map(int, input_data.split("..")))
b += 1  # включительно последнее число
print(random.random() * (b-a))

# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.
input_data = input("Введите границы для символов .. (ex: a..f): ")
a, b = tuple(input_data.split(".."))
delta = ord('z') - ord('a')
a = ord(a) - ord('a')
b = ord(b) - ord('a') + 1

alphabet = string.ascii_lowercase[a:b]

print(random.choice(alphabet))
