import queue

numbers = [10, 20, 30, 40, 50, 60, 70]
counter = 0     # 몇 개의 프로세스가 실행되었는지 카운팅

q = queue.Queue()

# 1, 2, 3, 4, 5
# 1
# 2, 3, 4, 5
# 2
# 3, 4, 5
# ...

for number in numbers:
    q.put(number)

result = 1
for number in numbers:
    result = result * q.get()

print(result)
# ------------------------------------------
# 왜 queue를 사용해야 하는가?
# 멀티스레드 실행 중일 때, 데이터에 대한
# 체계적인 송수신이 필요할 때 사용

# list, sequence와 유사한 자료구조


