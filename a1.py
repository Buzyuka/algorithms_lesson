# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

import cProfile


# 100 loops, best of 3: 88.1 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         3    0.000    0.000    0.000    0.000 a1.py:11(_test_number)
#         1    0.000    0.000    0.000    0.000 a1.py:8(original)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def original():
    a, b, c = 9, 4, 7

    def _test_number(target, a, b):
        if a < target < b or b < target < a:
            print(f"Число {target} среднее")

    _test_number(a, b, c)
    _test_number(b, a, c)
    _test_number(c, a, b)


# 100 loops, best of 3: 53.7 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 a1.py:28(sort_)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
def sort_():
    lst = [9, 4, 7]
    lst.sort()
    print(f"Число {lst[1]} среднее")


cProfile.run("sort_()")
