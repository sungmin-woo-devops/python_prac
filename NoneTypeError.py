def hi():
    print('hi')

def loop(f, n): # f repeats n times
    if n <= 0:
        return
    else:
        f()
        loop(f, n-1)

loop(hi, 5)
