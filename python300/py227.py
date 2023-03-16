def print_mxn(str, num):
    check_num = int(len(str) / num)
    for i in range(check_num + 1):
        print(str[i * num:i * num + num])

print_mxn("아이엠어보이유알어걸", 3)
