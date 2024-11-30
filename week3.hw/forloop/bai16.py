n = int(input("Nhap so phan tu: "))
sum = 0
for i in range (n):
    print ("Nhap phan tu trong danh sach: ")
    x = int(input())
    if x % 3 == 0:
        sum += x 
print ("Tong cac so chia het cho 3: ", (sum))