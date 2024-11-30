n = int(input("Nhap so gio lam: "))
if n < 0:
    print ("Thang nay khong co luong!")
elif n <= 40:
    print ("Luong thang nay la: ", (n * 2))
else:
    x = (40 * 2) + (n - 40)*4
    print ("Luong thang nay la: ", (x))