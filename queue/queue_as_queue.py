from queue import Queue

q = Queue(3)

q.put(3)
q.put(4)
q.put(5)
q.get()
print(q.qsize())