# 집합
# set() 함수를 이용하여 생성

# 1) 집합 생성
s1 = {1,2,3}
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

# 2) 리스트를 집합으로 변경
s2 = set([1,2,3]) 
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

# 왜 굳이 집합 자료형을 쓸까?
# 집합은 중복을 제거해준다.
s3 = set("Hello")
print(s3) # {'e', 'l', 'o', 'H'} - 집합은 순서가 존재하지 않는다.

# 집합의 특징
# 1. 중복 제거 2. 순서 없음

# 집합 사용 경우
# list -> set -> list 형태로 중복을 제거한 후 리스트로 변경

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1 & s2)             # and
print(s1.intersection(s2)) # 기준(s1), 비교 대상(s2)

# 합집합
print(s1 | s2)             # or
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 집합 관련 함수들
# 값 1개 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 요소 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1)

# frozenset() 함수를 이용하여 변경 불가능한 집합 생성 가능
s1 = frozenset([1,2,3])
print(s1, type(s1)) # frozenset({1, 2, 3}) <class 'frozenset'> - 수정 불가
# s1.add(4)           # AttributeError: 'frozenset' object has no attribute 'add'
s1.update([4,5,6])    # AttributeError: 'frozenset' object has no attribute 'update'
s2.remove(1)          # AttributeError: 'frozenset' object has no attribute 'remove'

# 리스트, 튜플 : 셋, 프로즌셋
