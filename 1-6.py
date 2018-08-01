# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

from functools import reduce
from memtool import *


def vars(names):
    return [(name.strip(), eval(name)) for name in names.split(",")]


n = input("введите трехзачное число: ")
nums = list(map(int, list(n)))
s = sum(nums)
f = reduce(lambda x, y: x * y, nums)

mem_trace(*vars("n, nums, s, f"))
print_mem_analyze()
