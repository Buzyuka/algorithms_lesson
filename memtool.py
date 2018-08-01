import sys

total_mem = 0
vars = {}


def _mem_trace(x, level=0):
    name, var = x

    global total_mem
    global vars

    size = sys.getsizeof(var)
    total_mem += size
    vars[name] = size + vars.get(name, 0)

    if hasattr(var, "__iter__"):
        if hasattr(var, "items"):
            for item in var.items():
                _mem_trace((name, item), level + 1)

        elif not isinstance(var, str):
            for item in var:
                _mem_trace((name, item), level + 1)


def mem_trace(*args):
    for arg in args:
        _mem_trace(arg)


def print_mem_analyze():
    global total_mem

    print(f"Общая выделенная память: {accumulator}")
    print(f"Переменные:")

    for name in vars.keys():
        print(f"{name}: {vars[name]}")
