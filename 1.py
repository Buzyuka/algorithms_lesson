# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# любому из чисел в диапазоне от 2 до 9.


def dividable(x):
    for i in range(2, 10):
        if x % i == 0:
            return True

    return False


seq = filter(dividable, range(2, 100))
print(len(list(seq)))
