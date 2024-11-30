import math
n = int(input("Nhap vao so n: "))
if n < 0:
       print("Nhap so nguyen duong!")
elif n < 2:
       print("{} khong la so nguyen to!".format(n))
       #note  format; ngắt vòng lặp
else:
    for i in range(2, int(math.sqrt(n+1))):
        if (n % i == 0):
               print("{} khong la so nguyen to!".format(n))
            # print(n, " khong la so nguyen to!")
            # dòng 10 và 11 tương đương nhau nhưng ưu tiên sử dụng dòng 10
            # khai báo được nhiều hơn
               break
        else:
           print("{} la so nguyen to!".format(n))
