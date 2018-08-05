# Алгоритм взят из книги: Т. Кормен Алгоритмы, построение и анализ
# Глава 9: медианы и порядковые статистики.

from random import random, randint

m = 5
n = 2*m + 1
arr = list(map(lambda _: randint(-100, 100), range(n)))


# Функция для выбора iй порядковой статистики
def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]

    q = rangomized_partition(arr, p, r)
    k = q - p + 1

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q+1, r, i - k)


def rangomized_partition(arr, p, r):
    i = randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def select(arr, i):
    return randomized_select(arr, 0, len(arr) - 1, i + 1)


median = len(arr) // 2

print(sorted(arr)[median])
print(select(arr, median))

assert(sorted(arr)[median] == select(arr, median))
