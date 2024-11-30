#sử dụng hàm isinstance để kiểm tra xem có phải số nguyên hay số thực.
a = [8, 9, 1.5, 1.7, "minh khue", "minh khoa" ]

songuyen = 0
sothuc = 0
chuoi = 0

for key in a:
    if isinstance (key, int):
        songuyen += 1 
    elif isinstance (key, float):
        sothuc += 1
    else:
        chuoi += 1

print ("So cac so nguyen: ", songuyen)
print ("So cac so thap phan: ", sothuc)
print ("So cac chuoi: ", chuoi)