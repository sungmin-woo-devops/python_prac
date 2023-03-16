def print_5xn_2(line):
    check_num = int(len(line) / 5)
    for x in range(check_num + 1):
        print(line[x * 5: x * 5 + 5])

def print_5xn_1(str):
    for i in range(len(str)):
        if i % 5 == 0 and i !=0:
            print("")
        print(str[i], end="")
    print("")

print_5xn_1("아이엠어보이유알어걸")
print_5xn_2("아이엠어보이유알어걸")
