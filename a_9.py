# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

input_data = input("Введите три числа через запятую: ")
a, b, c = tuple(map(int, input_data.split(",")))


def test_number(target, a, b):
    if a < target < b or b < target < a:
        print(f"Число {target} среднее")
        exit(0)


test_number(a, b, c)
test_number(b, a, c)
test_number(c, a, b)
