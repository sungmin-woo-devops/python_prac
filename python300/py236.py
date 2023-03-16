def 함수(num):
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)

print(c)
#  함수(b) -> 함수(a) -> 함수(10) 
#  (3)22      (2)18      (1)14
