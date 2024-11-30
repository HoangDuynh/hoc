n = int(input("Nhap nam duong lich: "))
if(n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
    #note vo cach tich hop dieu kien
    print("Nam vua nhap la nam nhuan: ", n)
else:
    print("Nam vua nhap khong phai la nam nhuan")