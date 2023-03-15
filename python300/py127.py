id = input("주민등록번호: ")

# 방법 1
temp = id.split("-")[1]
if temp[0] == "1" or temp[0] == "3":
    print("남자")
else:
    print("여자")

# 방법 2
front, back = id.split("-")

if int(back[0]) in [1, 3]:
    print("남자")
elif int(back[0]) in [2, 4]:
    print("여자")
