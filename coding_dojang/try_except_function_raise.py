def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)

try:
    three_multiple()
except Exception as e:
    print('예외가 발생합니다', e)