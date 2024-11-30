n = int(input("Nhap vao so dien: "))
#tạo biến mới để thay thế phép trong hàm
dien = 0
if(0<n<51): 
    dien = n * 1678
    print("so tien phai tra là: ", dien)
elif(n<101):
    dien = 50*1678 (n - 50)* 1734
    print("so tien phai tra là: ", dien)
else:
    dien = 50 * 1678 + 50*1734 (n - 100) * 2014
    print("so tien phai tra là: ", dien)