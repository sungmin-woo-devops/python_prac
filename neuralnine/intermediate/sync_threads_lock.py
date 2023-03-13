import threading
import time

# 목적: min, max 도달하기
x = 8192    # 전역 변수 설정

# 리소스에 대한 접근을 승인/금지
lock = threading.Lock()

# *2, /2 - 스레드 생성
def double():
    global x 
    lock.acquire()      # 리소스 접근 획득
    while x < 16384:
        x = x * 2
        print(x)
        time.sleep(1)   # 1초 대기 - 관찰 위해 시간 지연 추가
    print("Reached the maximum!")
    lock.release()      # 리소스 접근 해제

def halve():
    global x
    lock.acquire()
    while x > 1:
        x = x / 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
# ------------------------------------------------------------
# x를 컴퓨팅 자원이라 생각하자.
# 다수의 쓰레드가 컴퓨팅 자원에 동시에 접근하지 못하도록 lock
