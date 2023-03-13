array = [[0 for col in range(11) for row in range(10)]]
array2 = [[0]*11 for i in range(10)]

for i in array:
    for j in i:
        print(j, end=" ")
    print()
