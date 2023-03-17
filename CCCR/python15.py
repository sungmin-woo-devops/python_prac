# 반복문
# 자동화를 의미
'''
for i in 시퀀스자료형:
    수행문장1
    수행문장2

i는 변수(임의지정)    
'''

'''
for i in [1,2,3]:
    print(i)
1
2
3   
'''

test_list = [1,2,3]
test_tuple = (1,2,3)
test_str = "123"

# 반복문은 시퀀스 자료형에서 실행할 수 있다.
for i in test_list:
    print(i)
for i in test_tuple:
    print(i)
for i in test_str:
    print(i)

# print()의 end 인자
for i in test_list:
    print(i, end="")
for i in test_tuple:
    print(i, end="\t")

print("")
# for문 변수에 다양한 자료형 사용 가능
a = [(1,2), (3,4), (5,6)]
for (a, b) in a:
    print(a + b)

# 5명의 시험점수가 각각 90, 25, 67, 45, 80점
# 60점 이상이면 합격 아니면 불합격을 통보하는 코드
# 1번 학생은 합격입니다.
# 2번 학생을 불합격입니다.

scores = [90, 25, 67, 45, 80]

# 내 풀이
for score in scores:
    if score >= 60:
        print(f'{scores.index(score)+1}번 학생은 합격입니다.')
    else:
        print(f'{scores.index(score)+1}번 학생은 불합격입니다.')

# 강사님 풀이
number = 0
for score in scores:
    number = number + 1
    if score >= 60:
        print(f'{number}번 학생은 합격입니다.')
    else:
        print(f'{number}번 학생은 불합격입니다.')

# 3번 풀이
scores = [90, 25, 67, 45, 80]

for i in range(len(scores)):
    if scores[i] >= 60:
        print(f"{i+1}번 학생은 합격입니다.")
    else:
        print(f"{i+1}번 학생은 불합격입니다.")

# continue
# 반복문을 끝내지 않고 반복문 초기로 돌아가게 하는 구문
# 반복은 이어서 진행
for i in [1,2,3,4,5]:
    if i >= 3:
        print(i)
    else:
        continue

scores = [90, 25, 67, 45, 80]

number = 0
for score in scores:
    number = number + 1
    if score < 60:
        continue
    else:
        print(f'{number}번 학생은 합격입니다.')

# for문과 자주 같이 쓰이는 range()
# range() 함수는 범위를 의미
# 인자 1~3개 들어올 수 있다.

# range(10) -> 0 ~ 9          # 첫번째 인자에 0 생략
# range(1,10) -> 1 ~ 9
# range(1,10,2) -> 1,3,5,7,9  # 세번째 인자는 step

print(range(10), type(range(10)))
print(list(range(10)))

print(range(1,10))
print(list(range(1,10)))

print(range(1, 10, 2))
print(list(range(1, 10, 2)))

# 위의 성적 관리 코드를 간단하게 구현할 수 있음
scores = [90, 25, 67, 45, 80]
number = 0
for i in range(len(scores)):
    if scores[i] < 60:
        continue
    else:
        print(f'{i+1}번 학생은 합격입니다.')

# 리스트 안에 요소 담기
# 기본: 빈 리스트에 append()
a = [1,2,3,4,5]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 리스트 안에 for문 사용하여 간단하게 구현 가능
a = [1,2,3,4,5]
result = [num * 3 for num in a]
print(result)

result2 = [b * b for b in a]
print(result2)

# 리스트 안에 for문과 if문 혼합 사용 가능
# (3)[num * 3 (2)for num in a (1)if num % 2 == 1]
# (1)for문에서 (2)if문 사용 후 (3)연산
a = [1,2,3,4,5]
result = [num * 3 for num in a if num % 2 == 1]
print(result)

# 리스트 안에 for문과 if-else문 혼합 사용 가능
# 연산 / if-else문 / for문 순서로 바뀜
# 처리 순서는 (1)for문 (2)if-else문 (3)연산이다. 
a = [1,2,3,4,5]
result = [num * 3 if num % 2 == 1 else 0 for num in a]
print(result)

# 이중 for문
for i in [1,2,3]:
   for j in [4,5,6]:
       print(i, j)

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(f'{i * j}', end="\t")
    print("")