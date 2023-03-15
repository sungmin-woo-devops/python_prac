mul = 1
for i in range(1,11):
    mul = mul * i
print(mul)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))

