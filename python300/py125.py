user = input("휴대전화 번호 입력: ")
num, *temp = user.split("-")

if num == "011":
    telecom = "SKT"
elif num == "016":
    telecom = "KT"
elif num == "019":
    telecom = "LGU"
else:
    telecom = "알수없음"

print(f"당신은 {telecom} 사용자입니다.")
