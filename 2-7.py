import random
from math import floor


def _merge(a1, a2):
    merged = []
    n = len(a1) + len(a2)
    i, j = 0, 0

    a1.append(float("inf"))
    a2.append(float("inf"))

    for _ in range(n):
        if a1[i] <= a2[j]:
            merged.append(a1[i])
            i += 1
        else:
            merged.append(a2[j])
            j += 1

    return merged


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    q = floor(len(arr) / 2)
    a1 = merge_sort(arr[0:q])
    a2 = merge_sort(arr[q:])

    return _merge(a1, a2)


arr = list(map(lambda _: random.random() * 49, range(0, 100)))
print(merge_sort(arr))
