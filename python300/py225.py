my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dic, date):
    print(dic[date])

print_value_by_key(my_dict, "10/26")
