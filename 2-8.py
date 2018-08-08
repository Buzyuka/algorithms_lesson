# Ответ расходится с ответом из презентации, потому что
# дерево можно построить по разному из одной и той же последовательности
# к примеру, в презентации очередь получилась такая:
# ['r', '!', 'p', '0', ' ', 'b', 'e']
# PriorityQueue же отдает в такой последовательности:
# ['r', '!', 'p', ' ', 'o', 'b', 'e']
# По длине же получилось то же самое.

from collections import Counter
from queue import PriorityQueue


class Node:
    def __init__(self, value, priority, left=None, right=None, parent=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.parent = parent
        self.code = None

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __cmp__(self, other):
        return self.priority == other.priority

    def __repr__(self):
        return f"Node[value={self.value}, priority={self.priority}, " \
               f"left={self.left}, right={self.right}]"

    def get_code(self):
        """
        Будем подниматься снизу вверх.
        """
        if self.code is not None:
            return self.code

        code = ""
        parent = self.parent
        child = self

        while parent is not None:
            if parent.left == child:
                code += "0"
            elif parent.right == child:
                code += "1"
            else:
                raise AssertionError("Такого не должно быть")

            child = parent
            parent = parent.parent

        # Запоминаем получившийся код, чтобы лишний раз не
        # обходить дерево, reversed, т.е. мы шли снизу.
        self.code = list(reversed(code))
        return self.code


def build_tree(seq):
    queue = PriorityQueue()
    letter_nodes = {}

    for value, count in Counter(seq).items():
        node = Node(value=value, priority=count)
        queue.put(node)
        letter_nodes[node.value] = node

    root = None

    while not queue.empty():
        left = queue.get()
        right = queue.get()

        root = Node(
            value=None,
            priority=left.priority + right.priority,
            left=left,
            right=right
        )

        left.parent = root
        right.parent = root

        if queue.empty():
            break

        queue.put(root)

    return root, letter_nodes


def haffman_encode(seq):
    tree, letter_nodes = build_tree(seq)
    codes = []

    for char in seq:
        code = letter_nodes[char].get_code()
        codes.append("".join(code))

    print(" ".join(codes))


input_data = "beep boop beer!"
haffman_encode(input_data)
