def bang_cuu_chuong (n):
    if n < 1:
        return False
    else:
        for i in range (1, n+1):
            for j in range (1, n+1):
                return ((i), "x", (j), "=", (i*j))