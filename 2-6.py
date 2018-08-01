# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# загаданного введенное пользователем число. Если за 10 попыток число не отгадано,
# то вывести его.

import random
from memtool import *


def vars(names):
    return [(name.strip(), eval(name)) for name in names.split(",")]


num = random.randint(0, 100)
success = False

help_messages = {
    True: "Загаданное число меньше",
    False: "Загаданное число больше"
}

result_messages = {
    True: "Вы угадали",
    False: "Попытки кончились"
}

mem_trace(*vars("num, success, help_messages, result_messages"))

for i in range(0, 10):
    guess = int(input("Угадайте число: "))
    mem_trace(*vars("guess, i"))

    if guess == num:
        success = True
        break
    else:
        print(help_messages[num < guess])

print(result_messages[success])
print_mem_analyze()
