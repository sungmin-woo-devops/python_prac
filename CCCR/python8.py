# 리스트 관련 함수들

# 리스트 요소 추가(append)
a = [1,2,3]

# None, a 리스트에 4를 1)추가하고 2)본다.
a.append(4)
print(a)

print(a.append(4))

# 리스트에 리스트 추가
a = [1,2,3]
a.append([4,5])
print(a)

# 리스트 정렬(sort)
a = [1,4,2,3]
a.sort()       # 리스트가 정렬 후 변경된 사항이 저장됨
print(a)

# 정수형과 문자열은 다른 자료형이기 때문에 비교 불가 -> 연산 불가
# a = ['abc', 123, 'you need python']
a = ['abc', '123', 'you need python']
a.sort() 

# 문자의 순서는 유니코드를 기반으로 한다.
print(a)

# 리스트 뒤집기(reverse)
a = [1,4,2,3]
a.reverse()
print(a)

# 내림차순 정렬을 원할 경우 1)오름차순 후 2)뒤집기
a = [1,4,2,3]
a.sort()
a.reverse()
print(a)

# 리스트에서 요소 찾기(index, find X)
# 문자열은 index, find 모두 사용 가능
a = [1,4,2,3]
print(a.index(2)) # 검색의 기능 / 변경하지 않음

# 리스트 사이에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)
print(a)

# 1과 2 사이에 해당 리스트를 통째로 삽입
a = [1,2,3]
a.insert(1,['a','b','c'])
print(a)

# 리스트 요소 제거(remove) - 값을 기준으로 제거
# 기존에는 인덱싱을 이용하여 요소 제거
a = [1,2,3,1,2,3]
a.remove(3) # 3번 위치 제거 X, 값이 3인 요소 제거 
print(a)

a.remove(3) # 한번에 한 요소 삭제
print(a)

# 라스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop())  # 맨뒤 요소 추출(return) 
print(a)        # 기존 리스트에서 제거

a = [1,2,3]
print(a.pop(1)) # 인덱스 1번의 요소를 pop
print(a)

# 리스트에 포함된 요소 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))

# 리스트 확장(extend) - 하나의 리스트에서 확장
# extend vs append (append한 대상 자체가 하나의 요소)
a = [1,2,3]
a.extend([4,5])
print(a)

# extend와 더하기(+)는 똑같다.
a = [1,2,3]
a = a + [4,5]
print(a)

# 리스트의 가장 큰 핵심 - 변경이 가능하며 요소를 담는 자료형













