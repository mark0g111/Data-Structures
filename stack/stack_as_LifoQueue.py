from queue import LifoQueue


class MyQueueStack:
    def __init__(self, length):
        self.array = LifoQueue(maxsize=length)

    def push(self, element):
        self.array.put(element)

    def pop(self):
        element = self.array.get()
        return element

    def peek(self, index):
        pass

    def empty(self):
        if self.array.qsize() == 0:
            return True
        return False

    def size(self):
        return self.array.qsize()

    def __str__(self):
        return str(self.array)


s = MyQueueStack(10)
s.push(2)
s.push(3)
s.push(4)
print(s.size())

print(s.empty())
print(s)
