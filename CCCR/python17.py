# 함수
# 재사용하기 위한 용도
# 코드 분리 목적
def add(a, b):
    a + b

print(add(1,2)) # None

# return 존재: 반환값 있는 함수
# 입력값과 출력값이 있는 함수
def add(a,b):
    return a + b

print(add(1,2)) # 3

# return 존재 X: 반환값 없는 함수
# 매개변수 vs. 인자
def add2(a, b):
    print(a+b)

# 결과값이 아닌 단순 출력값 
add2(3,4)        # 7
print(add2(3,4)) # 함수실행 결과:7, 
                 # 함수 종료 후 반환값 없음: None

# 매개변수 X / 반환값 O
def test():
    return 10

test()           # 10
print(test())    # 10

# 매개변수 X / 반환값 X
def test2():
    print("Hello")

test2()         # Hello = 출력값
print(test2)    # Hello, None = 반환값 X

# append : 입력값 O, 반환값 X
a = [1,2,3]
print(a.append(4)) # None
print(a)           # [1,2,3]

# return으로 여러 값 전달 가능
def swap(a, b):
    return b,a

# 여러 값을 하나의 튜플로 반환
print(swap(10, 20), type(swap(10,20)))

# 인자의 기본값 지정
# b의 매개변수에 초기 인자를 대입하여 입력은 선택사항이 됨
def add(a, b=1):
    return a + b

print(add(1))
print(add(4,5))

# 키워드 인수
# 기본적으로 인자의 위치를 맞춰 넣어줘야 하는데
# 그럴 경우 불편하기 때문에 인자들을 키워드로 구분하여 순서 상관 없이
# 입력하기 위해 사용한다.

def area(height, width):
    return height * width

print(area(10, 20))

# 키워드 인수로 인자 입력
print(area(height=10, width=7))
print(area(width=4, height=8))

# 인자 입력 시 Positional 또는 keyword 둘 중 하나의 방식만 사용한다.
# 인자가 여러개일 경우 일부 인자만 키워드로 입력하게 되면 나머지 인자들에 대한 구분이 정확하지 않아 에러가 발생하게 된다.
# Positional argument cannot appear after keyword arguments
# print(area(width=109, 20))

# 키워드 인수 사용시 보통 인자가 먼저 오고 키워드 인수가 와야 함
print(area(10, width=20))
# 결국 핵심은 컴퓨터가 인자를 정확하게 구별해낼 수 있게 하는 코드를 작성해야 한다는 것이다.


# 가변 길이 인수 리스트(*매개변수)
def varlien(a, *b):
    return a, b

# *을 붙이면 인자가 '0개 이상' 올 수 있다는 뜻이다.
print(varlien(1))
print(varlien(1, 2))
print(varlien(1, 2, 3))
print(varlien(1, 2, 3, 4))


# 키워드 매개변수(**매개변수)
# 키/값 쌍을 매개변수에 인자로 넣으면 키를 사용해 값을 활용하게 된다.
def h(a,b,c,d):
    print(a,b,c,d)

# 딕셔너리의 값을 인자로 사용
dicargs = {'a': 1, 'b': 3, 'c': 5, 'd': 7}
h(**dicargs) # 1 3 5 7


# 함수의 변수화 - 자바스크립트 콜백 함수(?)
# 함수를 정의하는 순간 메모리에 적재됨 = 함수 또한 객체
def add(a, b):
    return a + b

addition = add
print(addition(1, 2))

