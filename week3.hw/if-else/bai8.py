n = int(input("Nhap vao so thang: "))
y = int(input("Nhap vao so nam: "))
if n < 0 and n > 13 or y < 0:
    print ("Vui long nhap so nam, so thang hop le!")
elif n == 2 :
    if(y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
        print ("Thang 2 co 29 ngay")
    else:
        print ("Thang 2 co 28 ngay")
elif n < 8 : 
    if n % 2 == 0:
        print ("Thang {} co 30 ngay".format(n))
    else :
        print ("Thang {} co 31 ngay".format(n))
else :
    if n % 2 == 0:
        print ("Thang {} co 31 ngay".format(n))
    else :
        print ("Thang {} co 30 ngay".format(n))