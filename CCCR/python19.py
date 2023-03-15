# 변수의 유효 범위
# 전역 변수 : 함수 밖에서 정의된 변수
# 지역 변수 : 함수 안에서 정의된 변수
# https://wikidocs.net/62
# https://soooprmx.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EC%9D%B4%EB%A6%84%EA%B3%B5%EA%B0%84%EC%97%90-%EB%8C%80%ED%95%B4-%EC%A7%80%EC%97%AD%EB%B3%80%EC%88%98%EC%99%80-%EC%A0%84%EC%97%AD%EB%B3%80%EC%88%98

# 변수 호출 순서
str = "global variable"

def func_1():
    str = 'local variable'
    print(str)

func_1() # local variable - 함수 내 둘 다 있으면 지역 변수가 우선

# 함수 내에서 전역 변수 호출
def func_2():
    print(str)

func_2()

# 1. 함수의 반환값을 전역 변수로 받아 사용(권장)
result = 0
def add(a, b):
    return a + b

result = add(1,2)
print(result)

# 2. 함수 내부에서 전역 변수를 바꾸는 방법
result = 0
def add(a, b):
    global result
    result = a + b
print(result)

add(5, 6)
print(result)

# 실험
# 전역 변수와 지역 변수가 있는 상태에서 global로 가져올 경우 결괴
'''
str = "global variable"

def func_1():
    str = 'local variable'
    global str # "str" is assigned before global declaration
    print(str)

func_1()
print(str)
'''

# 재귀 함수
# while문으로 작성한 코드를 더 간단하게 작성 가능하다.
# def hello():
#     print("hello world")
#     hello()

# hello()
# RecursionError: maximum recursion depth exceeded while calling a Python object


# 재귀 함수 예시: factorial
# n! = n * (n-1) * (n-2) * ... * 1
# 10! = 10 * 9 * 8 * ... * 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

# return은 함수 내에서 반복문의 break의 역할도 한다.


