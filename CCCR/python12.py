# 부울(bool)
# 참(True) or 거짓(False)

a = True
b = False

print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

print(1 == 1)  # True
print(2 > 1)   # True

# 여러가지 자료형에서 참과 거짓을 확인해볼 수 있다.
# "Python" -> True / "" -> False(빈 문자열)
# [1,2,3] -> True / [] -> False(빈 리스트)
# 튜플, 딕셔너리도 마찬가지
# 숫자 1 -> True / 숫자 0 -> False
# 딕셔너리 None -> False

# 참과 거짓 판별
if []:            # 빈 리스트는 거짓
    print("참")
else:
    print("거짓")

if [1,2,3]:       # 내용이 있으면 참
    print("참")
else:
    print("거짓")

# 부울 함수
# bool()에 넣은 값에 대해 참/거짓 판별 
print(bool([]))      # False
print(bool([1,2,3])) # True








