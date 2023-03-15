id_num = input("주민등록번호: ")
front, back = id_num.split("-")

temp = int(back[1:3])
if temp >= 0 and temp <= 8 :
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
