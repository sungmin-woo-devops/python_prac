id_num = input("주민등록번호: ")
id_num = "".join(id_num.split("-"))

check_num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

temp = 0
for i in range(len(check_num)):
    temp = temp + int(id_num[i]) * check_num[i]

if int(id_num[-1]) == 11 - temp % 11:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
