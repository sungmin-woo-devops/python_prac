sentence = "This is a test"
words_list = senetence.split()

num_string = "10 2 3 2 5 6"
num_string_list = num_string.split()
print(num_string_list)

num_list = num_string.split().map(Number)
print(num_list)
