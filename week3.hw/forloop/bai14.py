n = int(input("Nhap so: "))
if n < 0:
    print("So khong hop le")
else:
    a = 0
    b = 1
    print("Day Fibonacci la: ", end=" ")
    for i in range(n):  
        if a > n:
            break
        print(a, end=" ")
        a, b = b, a + b