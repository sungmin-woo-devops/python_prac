# 문자열 포매팅
# 문자열을 표현하는 방법

# 일반 문자열 표현
print("I eat 3 apples")

# 바로 대입
print("I eat %d apples" % 3)
print("I eat %s apples" % "three")

# 변수 대입
number = 3
print("I eat %d apples" % number)

# 2개 이상의 값을 대입
print("I eat 3 apples, so I was sick three days.")

number = 3
days = "three"
print("I eat %d apples, so I was sick %s days" % (number, days))

# 문자열 %를 표시하는 방법
print("Error is 98%")
print("Error is %d%%" % 98)

"""
%s : 문자열
%c : 문자 하나
%d : 정수
%f : 실수(부동소수점)
"""

# 이렇게 사용하면 파이썬의 편리하게 사용하자는 정신이 지켜지지 않는다.
# 이렇게 해서 등장한 것이 format() 함수이다.

# format() 함수를 사용한 포맷팅
print("11 22 33")
print("%d %d %d" % (11,22,33))

# 자료형에 대한 부분을 명시해주지 않아도 된다. format()이 대신 처리
print("{} {} {}".format(11, 22, 33))

print("four five six")
print("%s %s %s" % ("four", "five", "six"))
print("{} {} {}".format("four", "five", "six"))

# format() 함수 사용시 위치 지정 가능
number = 3
days = "three"
print("I eat %d apples, so I was sick %s days" % (number, days))
print("I eat {} apples, so I was sick {} days".format(number, days))
print("I eat {1} apples, so I was sick {0} days".format(number, days))

# 이것마저도 길다... f 문자열 포매칭(3.6 이상) - f string
print(f"I eat {number} apples, so I was sick {days} days")

# f 문자열 포매팅은 연산을 지원한다.
print(f"I eat {number + 1} apples, so I was sick {days} days")


# 문자열 포매팅 3가지 방법
# % 이용, format() 함수 이용, f-string 이용


# 문자열 관련 함수들
# 문자열 자체(객체)에서 가지고 있는 함수(메서드)
a = "hobby"
print(a.count("b"))

# (첫) 문자 위치 알려주기(find)
a = "python is the best choice"
print(a.find("b"))

# 문자 위치 알려주기(index)
a = "Python is the best choice"
print(a.index("b"))

# find() 함수는 없는 문자를 찾을 경우 -1 출력
# index() 함수는 없는 문자를 찾을 경우 에러 출력
print(a.find("j"))    # -1 출력
# print(a.index("j")) # 에러 발생

# 코드 실행의 지속/중단 여부를 결정할 때 find()와 index() 중 선택

# 문자열 삽입
a = ","
print(a.join("abcd"))

# 경로 표현시 join을 자주 사용하다.
# /home/user/project/mysite/pybo
# 문자열들을 리스트로 묶어줘야 한다. 
a = "/"
print("/" + a.join(["home", "user", "project", "mysite", "pybo"]))

# 파이썬은 대소문자 구별
# 문자열을 대문자로 변환
a = 'hi'
print(a.upper())

# 문자열을 소문자로 변환
a = "HI"
print(a.lower())

# 공백 제거
# 왼쪽 공백 제거
a = "  hi  "
print(a.lstrip())

# 오른쪽 공백 제거
print(a.rstrip())

# 양쪽 공백 제거
print(a.strip())

# 문자열 변경(replace)
a = "Life is too short"
print(a.replace("Life", "This Pen"))

# 문자열 나누기(split)
a = "Life is too short"
print(a.split(" "))


#  /home/user/project/mysite/pybo
a = "/home/user/project/mysite/pybo"
print(a.split("/"))