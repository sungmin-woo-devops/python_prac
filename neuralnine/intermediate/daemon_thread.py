import threading
import time

path = "daemon_thread_text.txt"   # 텍스트 저장할 파일 경로 정의
text = ""           # 출력 위한 문자열 정의

def readFiles():
    global path, text
    while True:
        with open("daemon_thread_text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for x in range(30):
        print(text)
        time.sleep(1)

# daemon 스레드 생성(daemon=True)
t1 = threading.Thread(target=readFiles, daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()
