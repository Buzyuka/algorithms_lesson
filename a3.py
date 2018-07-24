# Определить, какое число в массиве встречается чаще всего.

# pip install PyFunctional
from functional import seq
import cProfile


lst = [2, 2, 3, 1, 2, 4, 6, 7, 5, 3, 3, 1, 2, 3, 2, 0, 5, 3, 5, 6]


# 100 loops, best of 3: 12.4 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 a3.py:12(original)
#        20    0.000    0.000    0.000    0.000 a3.py:13(<lambda>)
#        20    0.000    0.000    0.000    0.000 a3.py:15(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#        20    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def original():
    count_lst = map(lambda x: lst.count(x), lst)
    list_with_count = zip(lst, count_lst)
    max_count = max(list_with_count, key=lambda x: x[1])

    return max_count[0]


# 100 loops, best of 3: 46 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 <string>:12(__new__)
#         1    0.000    0.000    0.000    0.000 <string>:31(__repr__)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:252(__subclasshook__)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:72(_check_methods)
#         1    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
#         2    0.000    0.000    0.000    0.000 _weakrefset.py:70(__contains__)
#         1    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
#         1    0.000    0.000    0.000    0.000 a3.py:30(chain)
#        20    0.000    0.000    0.000    0.000 a3.py:32(<lambda>)
#        20    0.000    0.000    0.000    0.000 a3.py:33(<lambda>)
#         1    0.000    0.000    0.000    0.000 abc.py:178(__instancecheck__)
#         1    0.000    0.000    0.000    0.000 abc.py:194(__subclasscheck__)
#         1    0.000    0.000    0.000    0.000 execution.py:17(evaluate)
#         3    0.000    0.000    0.000    0.000 lineage.py:11(__init__)
#         2    0.000    0.000    0.000    0.000 lineage.py:33(__len__)
#         1    0.000    0.000    0.000    0.000 lineage.py:41(__getitem__)
#         2    0.000    0.000    0.000    0.000 lineage.py:49(apply)
#         1    0.000    0.000    0.000    0.000 lineage.py:56(evaluate)
#         1    0.000    0.000    0.000    0.000 lineage.py:67(cache_scan)
#         1    0.000    0.000    0.000    0.000 pipeline.py:129(__getitem__)
#         1    0.000    0.000    0.000    0.000 pipeline.py:1347(to_list)
#         1    0.000    0.000    0.000    0.000 pipeline.py:168(_evaluate)
#         2    0.000    0.000    0.000    0.000 pipeline.py:1694(_wrap)
#         1    0.000    0.000    0.000    0.000 pipeline.py:176(_transform)
#         1    0.000    0.000    0.000    0.000 pipeline.py:190(sequence)
#         2    0.000    0.000    0.000    0.000 pipeline.py:199(cache)
#         3    0.000    0.000    0.000    0.000 pipeline.py:31(__init__)
#         1    0.000    0.000    0.000    0.000 pipeline.py:480(map)
#         1    0.000    0.000    0.000    0.000 pipeline.py:59(__iter__)
#         1    0.000    0.000    0.000    0.000 pipeline.py:770(max_by)
#         1    0.000    0.000    0.000    0.000 streams.py:32(__call__)
#         1    0.000    0.000    0.000    0.000 streams.py:49(_parse_args)
#         1    0.000    0.000    0.000    0.000 transformations.py:23(name)
#         1    0.000    0.000    0.000    0.000 transformations.py:35(map_t)
#         3    0.000    0.000    0.000    0.000 util.py:20(is_primitive)
#         1    0.000    0.000    0.000    0.000 util.py:49(is_namedtuple)
#         1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x107d2ddd8}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     14/13    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
#       9/7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        20    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
def chain():
    max_count = seq(lst)\
        .map(lambda x: (x, lst.count(x)))\
        .max_by(lambda x: x[1])

    return max_count[0]


# 100 loops, best of 3: 4.28 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 a3.py:89(linear)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def linear():
    max_count_number = None
    max_count = 0

    counts = dict()

    for x in lst:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

        if counts[x] > max_count:
            max_count_number = x
            max_count = counts[x]

    return max_count_number


cProfile.run("linear()")
