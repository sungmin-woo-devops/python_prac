import threading

def hello():
    for x in range(50):
        print("Hello")

t1 = threading.Thread(target=hello)
t1.start()

# t1이 종료되기 전에 아무것도 실행하고 싶지 않아!
# t1 스레드 먼저 수행해!
t1.join()

print("Another text")
