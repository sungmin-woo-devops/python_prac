import queue

data_queue = queue.LifoQueue()

data_queue.put("abc")
data_queue.put(1)

data_queue.qsize() # 2
data_queue.get() # 1 -> LIFO 구조이기 때문에 1이 먼저 출력

data_queue.qsize() # 1 -> 9번줄에서 1가 빠져나갔기 때문
data_queue.get() # abc 출력
