# 문자열 자료형
# 문자열 자료형을 만들기 위해서는 따옴표를 사용

a = "hello world"
b = "hello world"

print(a)
print(b)

# "python is very easy." he says 표현
a = '"Python is very easy." he says'
print(a)
b = "\"python is very easy\" he says"
print(b)

# \는 뒤의 기호를 특수 목적으로 사용하지 않게 만듦
c = "10000\\"
print(c)

# 문자열에서는 이스케이프 문자라는 특수한 기능이 존재
d = "hello\nworld"
print(d)

# 이스케이프를 많이 사용하면 가독성이 떨어지기 때문에 줄바꿈 시 다른 방법 사용
d = """
hello
world
"""
print(d)

# 이스케이프 코드
"""
\n : 줄바꿈
\t : 탭
\\ : 문자 \를 그대로 표현하고 싶을 때 사용
\' : 문자 '를 그래도 표현하고 싶을 때 사용
\" : 문자 "를 그래도 표현하고 싶을 때 사용
"""

# 문자열 더하기
head = "python"
tail = " is fun"
print(head + tail)


# 문자열 곱하기
print(head * 3)

# 문자열 곱하기 응용
print("=" * 20)
print("my program(v.11)")
print("=" * 20)

# 문자열의 길이 구하기
a = "Life is too short"
print(len(a))

# 숫자 + 문자의 결과?
# 연산하고 싶은 경우 데이터 유형을 일치시켜줘야 함
a = 1
b = "python"
# print(a+b)

# 문자열은 인덱싱과 슬라이싱이라는 개념이 존재
# 인덱싱은 자리에 맞춰 한가지 문자를 출력
# 슬라이싱은 자리에 맞춰 여러 문자를 출력
# 원하는 데이터를 추출, 가공하는데 사용된다.

# 문자열 인덱싱
a = "python is too short, You need Python"
print(a[10])
print(a[-6])

# 문자열 슬라이싱
a = "python"
print(a[0:4])

# 슬라이싱에서 첫 숫자를 생략하면 처음부터라는 의미
print(a[:4])

# 슬라이싱에서 끝 문자를 생략하면 끝까지라는 의미
print(a[2:6])
print(a[2:])

# 슬라이싱의 첫 숫자와 끝 숫자를 생략하면 처음부터 끝까지라는 의미
print(a[0:6])
print(a[:])

# 문자열 포매팅
# 문자열을 표현하는 방법

# 일반 문자열 표현
print("I eat 3 apples")

# 바로 대입
print("I eat %d apples" % 3)
print("I eat %s apples" % "three")





