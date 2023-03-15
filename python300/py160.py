리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    if i.split(".")[1] == "h" or i.split(".")[1] == "c":
        print(i)
