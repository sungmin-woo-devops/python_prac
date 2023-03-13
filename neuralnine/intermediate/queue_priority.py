import queue

q = queue.PriorityQueue()

q.put((2, "2시"))
q.put((11, "11시"))
q.put((1, "1시"))

print("q.get()----------")
while not q.empty():
    print(q.get())


q.put((2, "2시"))
q.put((11, "11시"))
q.put((1, "1시"))

print("q.get()[0]-------")
while not q.empty():
    print(q.get()[0])


q.put((2, "2시"))
q.put((11, "11시"))
q.put((1, "1시"))

print("q.get()[1]-------")
while not q.empty():
    print(q.get()[1])
