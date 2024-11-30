chuoi = input("Nhap chuoi: ")

demchu = 0
demso = 0

for x in chuoi :
    if x.isalpha():
        #kiểm tra ký tự có phải chữ
        demchu += 1
    elif x.isdigit:
        #kiểm tra ký tự có phải số 
        demso += 1

print ("So ky tu chu: ", demchu)
print ("So ky tu la so: ", demso)