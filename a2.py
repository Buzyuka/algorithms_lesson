# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и
# 2 нечетные (3 и 5).

import cProfile


numbers = list(map(int, "34560918394857192038572027364563983984861623859"))


# 100 loops, best of 3: 16 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 a2.py:11(original)
#        47    0.000    0.000    0.000    0.000 a2.py:12(<lambda>)
#        47    0.000    0.000    0.000    0.000 a2.py:13(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def original():
    even = list(filter(lambda x: x % 2 == 0, numbers))
    odd = list(filter(lambda x: x % 2 != 0, numbers))

    return even, odd


# 100 loops, best of 3: 6.11 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 a2.py:26(linear)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        47    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def linear():
    even = []
    odd = []

    for x in numbers:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even, odd


cProfile.run("linear()")
