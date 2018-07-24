import cProfile


# Для n = 1000
# 100 loops, best of 3: 22.2 msec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.021    0.021    0.021    0.021 primes.py:6(primes_1)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def primes_1(x):
    assert x > 1
    primes = []

    for i in range(2, x + 1):
        prime = True

        for j in range(2, x + 1):
            if i == j:
                continue

            if i % j == 0:
                prime = False
                break

        if prime:
            primes.append(i)

    return primes


# Для n = 1000
# 100 loops, best of 3: 829 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.001    0.001    0.002    0.002 primes.py:35(primes_2)
#       999    0.000    0.000    0.000    0.000 primes.py:36(<lambda>)
#       999    0.000    0.000    0.000    0.000 primes.py:53(<lambda>)
#       168    0.000    0.000    0.000    0.000 primes.py:54(<lambda>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def primes_2(x):
    numbers = list(map(lambda n: (False, n), range(2, x + 1)))
    p = 2

    while True:
        last_p = p

        for i in range(2*p, x + 1, p):
            numbers[i-2] = (True, i)

        for i in range(p + 1, x + 1):
            crossed, number = numbers[i-2]

            if not crossed:
                p = number
                break

        if p == last_p:
            filtered = filter(lambda n: not n[0], numbers)
            return list(map(lambda n: n[1], filtered))


cProfile.run("primes_2(1000)")
