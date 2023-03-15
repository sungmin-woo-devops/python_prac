my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(len(my_list) - 2):
    print( ( my_list[i] + my_list[i+1] + my_list[i+2] ) / 3)
