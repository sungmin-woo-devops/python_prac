num = int(input("입력값: "))

temp = num - 20
if temp < 0:
    print(f"출력값: 0")
elif temp >255:
    print(f"출력값: 255")
else:
    print(f"출력값: {temp}")

