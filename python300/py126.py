postal_code = input("우편번호: ")
gu = postal_code[:3]

if gu in ["010", "011", "012"]:
    print("강북구")
elif gu in ["013", "014", "015"]:
    print("도봉구")
elif gu in ["016", "017", "018", "019"]:
    print("노원구")
