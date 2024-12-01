def sum_even (n):
    s = 0
    for i in range (1 , n + 1):
        if i % 2 == 0:
            s += i
    return s
ex = (10000)
print (sum_even (ex))