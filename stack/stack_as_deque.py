from collections import deque


class MyDequeStack:
    def __init__(self):
        self.array = deque()

    def push(self, element):
        self.array.append(element)

    def pop(self):
        element = self.array.pop()
        return element

    def peek(self, index):
        return self.array[index]

    def empty(self):
        if len(self.array) == 0:
            return True
        return False

    def size(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

    def __iter__(self):
        self.index = len(self.array) - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result
