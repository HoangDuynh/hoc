n = int(input("Nhập số lượng học sinh: "))

myclass = {}

for i in range(n):
    ten = input("Nhập tên học sinh thứ {}: ".format(i+1))
    d = int(input("Nhập điểm của {}: ".format(ten)))
    #d = int(input("Nhập điểm của : ",))
    if d < 0 or d > 10:
        print("Điểm không hợp lệ. Vui lòng nhập lại.")
        continue
    myclass[ten] = d

dcount = {}
for d in myclass.values():
    if d in dcount:
        dcount[d] += 1
    else:
        dcount[d] = 1

print("Kết quả thống kê:")

for d, count in dcount.items():
    print(f"Số học sinh đạt {d} điểm: {count}")

print(dcount)
print(myclass)