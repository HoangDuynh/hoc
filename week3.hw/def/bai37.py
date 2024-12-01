import math

def filter_primes(list):
    primelist = []
    for n in list:
        if n < 2:  
            continue
        l = True
        for i in range(2, int(math.sqrt(n)) + 1): 
            if n % i == 0: 
                l = False
                break
        if l: 
            primelist.append(n)
    return primelist
ex = [1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 17]
print(filter_primes(ex))
