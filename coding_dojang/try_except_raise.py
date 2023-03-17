# https://dojang.io/mod/page/view.php?id=2400

# 예외 발생시키기

# 예외를 발생시킬 때는 raise에 예외를 지정하고 에러 메시지(생략 가능)를 넣는다.

try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.') # 예외를 발생시킴
    print(x)
except Exception as e:
    print("예외가 발생했습니다.", e)

# 결과
# 3의 배수를 입력하세요: 7
# 예외가 발생했습니다. 3의 배수가 아닙니다

# raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고
# 바로 except로 넘어간다. 따라서 try의 print(x)는 실행되지 않는다.