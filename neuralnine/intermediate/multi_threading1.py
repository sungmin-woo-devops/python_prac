import threading

def helloworld():
    print("Hello World")

def function1():
    for x in range(10):
        print("One")

def function2():
    for x in range(10):
        print("Two")

t1 = threading.Thread(target=helloworld) # 함수 참조O, 호출X
t1.start()

t2 = threading.Thread(target=function1)
t3 = threading.Thread(target=function2)

t2.start()
t3.start()
# -------------------------------------------------------
# 왜 스레드 사용의 이점은?
# 두 개 이상의 태스크(함수)를 병렬적으로 처리 가능

# 멀티 프로세싱
# 같은 프로세스, 같은 메모리 공간에 있으면서 
# 여러 태스크 실행 가능

# 사용 예시
# 게임 개발에서 키보드, 마우스 동시 입력
# 다양한 인게임 오브젝트의 동시 동작 구현 가능
