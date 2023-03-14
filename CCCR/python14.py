# if 조건문
# 조건문은 참과 거짓을 판단하는 문장
'''
if 조건문:
    실행할 문장1
    실행할 문장2
    ...
'''

# 비교 연산자
# x ( <, >, <=, >=, ==, != ) y

# 돈이 있는 상황에서 택시를 타는 상황
# if문은 조건문이 참일 때만 실행된다.
money = True
if money:        
    print("택시")

money = False
if money:
    print("택시")

'''
if 조건문:
    실행할 문장1
    실행할 문장2
    ...
else:
    실행할 문장3
    실행할 문장4
'''

money = 2000
if money >= 3000:
    print("택시")
else:
    print("걷기")

# and  or  not
# a and b -> 둘 다 참이어야 함
# a or b -> 하나만 참이면 참
# not a -> a가 참이면 거짓

# 현금 2000원 보유중이고 카드를 보유하고 있음
# 돈이 3000원 이상 있거나 카드를 보유중이면 택시를 타고 아니면 걸어 가야 하는 상황
cash = 2000
card = True
if cash >= 3000 or card == True:
    print("택시")
else:
    print("걷기")


# in / not in
# 요소 in 리스트
# 요소 in 튜플
# 요소 in 문자열

# 주머니(pocket)에 종이(paper), 핸드폰(cellphone), 현금(money)가 있다고 가정
# 만약 주머니에 현금이 있으면 택시를 타고, 아니면 걸어가야 하는 상황

pocket = ('paper', 'cellphone', 'money')
if 'money' in pocket:
    print("택시")
else:
    print("걷기")

'''
if 조건문:
    실행할 문장1
elif 조건문:
    실행할 문장2
elif 조건문:
    실행할 문장3
else:
    실행할 문장4
'''

# 주머니에 종이와 핸드폰이 있다고 가정
# 주머니에 돈이 있으면 택시를 타고 주머니에 돈은 없지만 카드가 있으면 택시를 타고
# 돈도 없고 카드도 없으면 걸어가야 하는 상황

pocket = ('paper', 'cellphone')
if 'money' in pocket:
    print("택시")
else:
    if 'card' in pocket:
        print("택시")
    else:
        print("걷기")

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걷기")

# 조건을 넘겨야 할 경우 pass문 사용
'''
pocket = ['path', 'money', 'cellphone']
if 'money' in pocket:
    에러 발생
else: 
    print("걸어 가라")
'''

# 반복문의 break와 비슷한 개념(pass는 이후 조건문 실행 X)
# continue는 반복문에서 사용하는 개념으로 반복문 처음으로 돌아간다.
pocket = ['path', 'money', 'cellphone']
if 'money' in pocket:
    pass
else: 
    print("걷기")

# 만약 pass 구문 앞에 문장이 있을 경우?
# pass가 단독으로 쓰인 경우 하위항목은 수행되지 않음
pocket = ['path', 'money', 'cellphone']
if 'money' in pocket:
    pass
    print("나머지도 다 꺼내라")
else: 
    print("걷기")

# break와 차이
# pass문 앞에 명령문이 있는 경우 pass는 무시됨
pocket = ['path', 'money', 'cellphone']
if 'money' in pocket:
    print("돈을 꺼내라")
    pass
    print("나머지도 다 꺼내라")
else: 
    print("걷기")
# 만약 pass 구문 앞에 문장이 있을 경우 문장 수행이 일어나고
# 문장 수행이 일어나는 순간 pass는 무시당함


# if문 한 줄로 작성
# 수행할 문장이 하나인 경우 if문을 한 줄로 작성 가능하다.
pocket = ['path', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("걷기")