import math

n = int(input("Nhap vao so nguyen duong n: "))

uocnto = []
kuocnto = []

if n <= 0:
    print ("Hãy nhập số nguyên dương!")
elif n < 2:
     print ("1 không phải là số nguyên tố!")
else:
    for i in range(2, n + 1):
        l = True
        for j in range (2, int(math.sqrt(i)+1)):
                if (i % j == 0):
                    l = False
                    break
        if l:        
            if (n % i == 0):
                uocnto.append(i)
            else: 
                kuocnto.append(i)

print (uocnto)
print (kuocnto)