# Пользователь вводит две буквы. Определить, на каких местах
# они стоят и сколько между ними находится букв.

input_data = input("Введите две буквы через запятую: ")
a, b = tuple(input_data.split(","))
delta = ord('z') - ord('a')


def pos_in_alphabet(l):
    return ord(l) - ord('a') + 1


print(f"Буква {a} находится на {pos_in_alphabet(a)} позиции")
print(f"Буква {b} находится на {pos_in_alphabet(b)} позиции")
print(f"количество букв между {a} и {b} = {ord(b)-ord(a)-1}")
6