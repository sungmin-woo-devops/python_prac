# filter 사용
def pickup_even(x):
    if x % 2 == 0:
        return x

print(list(filter(pickup_even, [1,2,3,4])))

# 원본 만든 후 람다화시켜 파일의 크기를 줄이는 형태로 사용한다.
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4])))
