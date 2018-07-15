# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

from functools import reduce

n = input("введите трехзачное число: ")
nums = list(map(int, list(n)))

s = sum(nums)
f = reduce(lambda x, y: x * y, nums)

print(f"сумма: {s}")
print(f"произведение: {f}")
