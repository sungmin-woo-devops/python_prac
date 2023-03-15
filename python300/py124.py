num1 = int(input("input number1: "))
num2 = int(input("input number2: "))
num3 = int(input("input number2: "))

max_num = 0
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
print(max_num)
