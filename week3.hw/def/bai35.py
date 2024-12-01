def count_ptu (list , char):
    count = 0
    for c in list:
        if c == char:
            count += 1
    return count
ex = [1 , 2 , 2 , 3 , 4 , 5 , 2 , 12 , 22 , 2]
print (count_ptu(ex , 2))