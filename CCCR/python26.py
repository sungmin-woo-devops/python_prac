# 외장함수
# sys
# 시스템 제어

# 1. sys.argv
# 명령행에서 인자 전달
import sys
print(sys.argv)

# [w@arch python]$ python3 CCCR/python25.py apple pizza chicken
# ['CCCR/python25.py', 'apple', 'pizza', 'chicken']

print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# sys.argv 활용 예
# 홈페이지 자동 로그인 코드

#################################################################

# 2. sys.exit
# 코드 종료
# sys.exit()

print("hello") # 코드 종료되어 실행되지 않음

#################################################################

# pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장 및 불러오기 가능

# 파일을 하나 생성하여 [1,2,3]을 write하면 어떻게 될까?
# test.txt <- [1,2,3]

# 파일 안에 입력한 [1,2,3]은 리스트처럼 생겼지만 사실은 문자열이다.

# 진짜 리스트를 넣고 싶다면 어떻게 해야할까?
# 하지만 에러 발생 write() argument must be str, not list
'''
with open("CCCR/list.txt", "w") as f:
    f.write([1,2,3])
'''

# pickle을 이용하면 리스트 자체를 파일에 저장할 수 있다.
# 텍스트 형태가 아니라 바이너리 형식으로 write되게 된다.
import pickle

# 지정한 데이터를 직렬화하여 바이너리 파일로 write
with open("CCCR/list.txt", "wb") as f:
    pickle.dump([1,2,3], f)

# 바이너리 파일을 다시 텍스트 형태로 변환하여 로드
with open("CCCR/list.txt", "rb") as f:
    data = pickle.load(f)

print(data)

# https://docs.python.org/ko/3/library/pickle.html

#################################################################

# os
# 환경변수나 파일, 폴더 등 OS 자원을 관리
import os
print(os.environ)
print("")

# 환경변수 지정 가능
# 실행 파일이 들어가는 환경변수 확인
print(os.environ['PATH'])
print("")
print(os.environ['PATH'])
print("")
print(os.getcwd())
print("")
print(os.system("ls"))

print(os.system("pwd"))
# /home/w/Workspace/python
# 0 성공했다는 exit code

# 디렉터리 생성 및 삭제
# 만들 때 이미 있는지 없는지 확인 exists -> mkdir
os.mkdir("CCCR/test_dir")
os.rmdir("CCCR/test_dir")

os.unlink("foo.txt")
os.rename("list.txt, list2.txt") # 바꿔줄 애, 바꿀 이름

#################################################################