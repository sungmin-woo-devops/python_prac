리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in 리스트:
    filename ,extension = i.split(".")
    print(filename)
