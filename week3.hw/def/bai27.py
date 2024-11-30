def Fibonacci (n):
    if n < 0:
        return ("So khong hop le")
    elif n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n):  
            if a > n:
                break
            a, b = b, a + b
        return ("So Fibonacci thu ", (n), "la: ", (b))