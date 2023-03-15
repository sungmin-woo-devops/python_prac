# while문
# while 조건식:
#   코드1
#   코드2
#   코드3
# 조건식이 맞지 않는 상황이 되면 종료가 된다.
# 만약 조건식이 계속 참으로 유지된다면 무한루프를 돌게 된다.

# 10번 찍어 안 넘어가는 나무 없다
tree_hit = 0
while tree_hit < 10:
    tree_hit = tree_hit + 1
    print(f'{tree_hit}번 찍었습니다!')
print("나무 넘어갑니다!")

# 강사님 풀이
tree_hit = 0
while tree_hit < 10:
    tree_hit = tree_hit + 1
    print(f'나무를 {tree_hit}번 찍었습니다.')
    if tree_hit == 10:
        print(f"나무 넘어갑니다.")

prompt='''
1. Add
2. Del
3. List
4. Quit

Enter Number: 1
'''

# input()으로 받은 값은 항상 문자열로 저장된다.
'''
choice = 0
while choice != 4:
    print(prompt)
    choice = int(input("Enter Choice"))
'''

# 반복을 강제로 그만하고 싶을 때 break 구문 사용
# 커피자판기에 커피가 10잔 있고 수중에 3000원 있으며 커피 가격은 100원이라고 가정
'''
남은 돈은 2900원입니다.
돈을 받았으니 커피를 줍니다.
남은 커피는 9잔입니다.
...
커피가 다 떨어졌습니다. 판매를 중단합니다.
'''
coffee_stock = 10
coffee_price = 100
money = 3000

while money:
    if coffee_stock > 0:
        money = money - 100
        print(f"남은 돈은 {money}원입니다.")
        
        print(f"돈을 받았으니 커피를 줍니다.")

        coffee_stock = coffee_stock - 1
        print(f"남은 커피는 {coffee_stock}잔입니다.")
    else:
        print("커피가 다 떨어졌씁니다. 판매를 중단합니다.")
        break

# 1 ~ 10까지의 숫자에서 홀수만 출력하는 코드
# 방법 1
num = 0
while num < 10:
    num = num + 1
    if num % 2 == 1: print(num)

# 방법 2
num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)

# while문은 무한루프 가능
'''
while True:
    print("무한루프")
'''

