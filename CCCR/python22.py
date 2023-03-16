# 모듈
# 객체들(변수, 함수, 클래스)의 집합
# 파이썬 파일

import mod1

print(mod1.add(3, 5))

# as를 이용하여 긴 파일명을 줄여서 사용 가능
import mod1 as m

print(m.add(3, 5))

# if __name__ == "__main__":
# 현재 작업하고 있는 파일(환경)이 main이라는 뜻

print(__name__)


# if __name__ == "__main__":
# 자기 자신의 파일을 직접 실행시킨 경우와 모듈로 불러서 사용할 때를 분리

import test 
# import하면서 실행된 print(__name__)의 결과는 test가 출력됨
# main 작업 공간은 python22, import된 test는 모듈로 
# test에서 실행된 코드의 __name__, 즉 작업 환경은 test


# 클래스, 변수, 함수를 포함한 모듈 사용
import mod2
print(mod2.PI)

a = mod2.Math()    # 클래스의 객체화
print(a.solve(10)) # 반지름의 길이가 10인 원의 넓이

b = mod2.Math()
print(mod2.Math.solve(b, 2)) # self 매개변수 사용하여 객체 생성 
print(mod2.add(mod2.PI, 10))

# 내장 모듈
import os # 운영체제 관리 모듈

# 사용 가능한 모듈 경로
import sys # 시스템 관리 모듈

print(os.path) # <module 'posixpath' from '/usr/lib/python3.10/posixpath.py'>
print(sys.path) 
# ['/home/w/Workspace/python/CCCR', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', 
# '/home/w/.local/lib/python3.10/site-packages', '/usr/lib/python3.10/site-packages']

'''
[w@arch python300]$ find / -name "os.py" 2> /dev/null
/home/w/.cache/blender-benchmark-launcher/blender-versions/f9aaf69339e4aad3b7927a4cf7ba372453e393df662c92bc1fedf94e0c6b5382/blender-3.4.0-linux-x64/3.4/python/lib/python3.10/os.py
/home/w/miniconda3/pkgs/python-3.9.12-h12debd9_0/lib/python3.9/os.py
/home/w/miniconda3/lib/python3.9/os.py
/usr/lib/python2.7/os.py
/usr/lib/python3.10/os.py
/opt/anaconda/pkgs/python-3.9.13-haa1d7c7_1/lib/python3.9/os.py
/opt/anaconda/lib/python3.9/os.py
'''

# 모듈 사용 경로 추가
# /home/user 내 파이썬 파일도 모듈 경로로 추가하고 싶은 경우 
# append() 명령어를 사용한다.
# sys.path.append("/home/user")
# print(sys.path)

# 모듈 사용 경로 제거
# sys.path.remove(sys.path[-1])
# print(sys.path)

# 파이썬에서 특정 모듈의 위치 확인 가능
import os
import inspect

print(inspect.getfile(os))
print(inspect.getfile(inspect))