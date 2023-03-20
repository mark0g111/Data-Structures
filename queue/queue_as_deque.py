from collections import deque

d = deque('ghi')
d.append(4)
d.appendleft(1)
print(d)
print(d.count(1))
print(len(d))
