import threading
import time

# 리소스에 대해 5건의 접근만 가능
semaphore = threading.BoundedSemaphore(value=5)

# threading에 사용할 access 함수 정의
def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(2)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)

# NeuralNine - Python Intermediate Tutorial #4 - Synchronizing Threads
# https://www.youtube.com/watch?v=F3-bJlYWeJc
