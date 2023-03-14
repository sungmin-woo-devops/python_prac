# 튜플
# 소괄호(()) 이용
# 리스트와 다르게 요소 변경이 불가능하다. - 내용 변경 불가능
# 변경은 불가하지만 검색 등 연산은 가능하다.

# 튜플 사용 이유? 
# 고정된 메모리를 사용하기 때문(효율적인 메모리 사용)
# 내용 함부로 수정 불가능 -> 보안성
a = ()
b = (1)
b2 = (1,)
c = (1,2,3)
d = 1,2,3 # 튜플임을 자동으로 인식함

print(type(a))     # <class 'tuple'>

# 요소 1개 튜플 생성 시 뒤에 쉼표(,)를 넣어줘야 한다.
print(type(b))     # <class 'int'>
print(type(b2))

print(type(c))     # <class 'tuple'>
print(d, type(d))  # <class 'tuple'>

# 리스트 안에 튜플 생성 가능
a = [1, 2, 3,(4,5)]

# 튜플 안에 리스트 생성 가능
a = (1,2,3,[4,5]) # 어짜피 변경 불가한데 리스트를 포함? 튜플로 넣자.
a = (1,2,3,(4,5))
print(a)

# 튜플의 수정과 제거
a = (1,2,3)
# del a[1] 
# TypeError: 'tuple' object doesn't support item deletion

# a[1] = 4
# TypeError: 'tuple' object does not support item assignment

# 튜플의 인덱싱과 슬라이싱
a = 1,2,3
print(a[1])
print(a[:2])

# 튜플의 더하기, 곱하기 가능
a = 1,2,3
b = 4,5
print(a + b)
print(a * 3)

# 패킹과 언패킹
# 리스트와 튜플의 공통적인 부분

# 패킹
# 하나의 데이터에 여러 데이터를 넣는 것
# a = [1,2,3], a = (1,2,3) 요소들을 묶어다 a라는 변수에 할당

# 언패킹
# 한 데이터에서 여러 데이터를 꺼내오는 것
# b,c,d = a // a의 1,2,3을 각각 변수 b,c,d에 할당
T1 = (1,2,3,4,5)
a, b, c, d, e = T1

print(T1)
print(a,b,c,d,e)

# 언패킹에서는 하나의 데이터를 담고 나머지 데이터를 담을 수 있음
a, *b = T1
print(a,b)
print(b)    # 나머지 데이터는 리스트 형태로 저장됨

# 튜플과 리스트 변경
T = (1,2,3,4,5)
L = list(T) # 요소 변경하겠다.
print(L, type(L))

T = tuple(L) # 요소 변경 안하겠다.
print(T, type(T))

# 튜플: 소괄호, 내용 수정이 불가능함
