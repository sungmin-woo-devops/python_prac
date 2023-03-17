# 변수명 만들기
# 변수 = 값
# 변수의 첫 문자는 영문자 혹은 언더바(_)로 시작해야 함

# 변수의 첫문자로 숫자 사용 불가
# 1_unit = 1

# 변수의 첫문자로 특수 문자 사용 불가
# @_unit = 1

# 변수의 첫문자로 언더바 사용 가능
_unit = 1

# 변수로 예약어는 사용 불가
# and = 1
# for = 1

# 변수로 내장함수 이름 사용 가능
# 내장 함수 아닌 변수로 쓰였음
abs = 1
print(abs)

# 이제 내장 함수가 이닌 변수이기에 실행 시 에러 발생
# print(abs(-2))

# 변수에서 다시 내장함수 기능으로 원복하고 싶은 경우 del 키워드 사용
del abs
print(abs(-2))

# 파이썬에서 변수를 지정할 때 자동으로 데이터 타입이 지정됨
number = 1
pi = 3.14
flag = True
char = 'x'
chars = "hello"

# 변수의 데이터 타입 확인
print(chars)
print(type(number))
print(type(pi))
print(type(flag))
print(type(char))
print(type(chars))

# 변수 제거
del(number)
print(number)