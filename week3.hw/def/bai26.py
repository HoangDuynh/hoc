def bang_cuu_chuong (n):
    if n < 1:
        return False
    else:
        for i in range (1, n+1):
            for j in range (1, n+1):
                print ((i), "x", (j), "=", (i*j))
        return True
ex = (10)
print (bang_cuu_chuong(ex))