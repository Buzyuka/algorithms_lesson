import random


def bubble_sort(arr, comparator = lambda x, y: x > y):
    res = list(arr)
    swaped = False

    for i in range(len(res) - 1):
        for j in range(len(res) - i - 1):
            if comparator(res[j], res[j+1]):
                res[j], res[j+1] = res[j+1], res[j]
                swaped = True

        if not swaped:
            return res

    return res


arr = map(lambda _: random.randint(-100, 99), range(0, 100))
print(bubble_sort(arr, lambda x, y: x < y))
