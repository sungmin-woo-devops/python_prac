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
# gor문 변수에 다양한 자료형 사용 가능
a = [(1,2), (3,4), (5,6)]
for (a, b) in a:
    print(a + b)

