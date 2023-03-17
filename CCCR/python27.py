# shutil 
# https://wikidocs.net/149330

# 파일을 복사해주는 기능
import shutil
shutil.copy("CCCR/list.txt", "CCCR/list2.txt")

#################################################################

# glob
# 패턴을 사용하여 현재 디렉터리 및 하위 경로의 파일들 검색
# https://wikidocs.net/153155

import glob
result = glob.glob("/home/w/Workspace/python/CCCR/list*")
print(result)

#################################################################

# time
# 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초 단위로 반환
# https://wikidocs.net/3140
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
time.sleep(1)

# 1. 파일 이름에 날짜 들어갈 때 사용
# 2. 랜덤값 생성 시 사용 - 겹치지 않는 파일명 등... 생성 가능

# time.sleep()
# 자동화 코드 동작에서 여유 시간을 둘 때 자주 사용됨

# datetime
# https://dojang.io/mod/page/view.php?id=2463


# calendar
# https://kingmaron.tistory.com/61
import calendar
calendar.calendar(2023)
calendar.prmonth(2008, 12)

#################################################################

# random
# https://www.daleseo.com/python-random/
# https://aplab.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-random
# 실행 시마다 숫자 달라짐
# 0보다 크거나 같고 1보다 작은 실수 값을 반환
import random
print(random.random())
print(random.randint(1, 5))

# random.choice()
# https://ponyozzang.tistory.com/702
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

data = [1, 3, 5, 7, 9]
while data:
    print(random_pop(data))

# random.choices()
# 가중치를 부여해 확률적으로 값을 가져옴
# 확률은 100을 기준으로 함(총합 100)
print(random.choices(range(1, 6), [5, 5, 5, 5, 80]))


# random.uniform()
# 범위를 지정해 랜덤한 실수 값을 받음
print(random.uniform(10, 20))


# random.shuffle()
# 리스트 내 데이터를 섞어주는 역할을 함
# 리스트 내 자료형이 정수, 문자열, 무엇이든 상관 X
data = [1,2,3,4,5]
random.shuffle(data)
print(data)

#################################################################

# webbrowser
# 파이썬의 webbrowser 모듈은 웹 브라우저를 제어할 수 있는 기능을 제공
import webbrowser

# 단순하게 웹 페이지를 띄어주는 역할만 함
webbrowser.open("https://www.google.com")









