n = int(input("Nhap so: "))
if n < 2:
    print ("So khong hop le")
elif n == 2:
    print ("So nguyen to: ", (n))
else :
    print ("So nguyen to: ",end= ' ')
    for i in range (2, n+1):
        l = True
        for j in range (2, int(i/2 + 1)):
            if i % j == 0:
                l = False
                break
        if l :
                print (i,end= ' ')