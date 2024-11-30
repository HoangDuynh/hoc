"""
1. Mang 
2. Dictionary
2. Libs
"""

a = 5 # int : so nguyen 
b = 5.6 # float / double : so thuc
c = "So nguyen to" # string :chuoi

print(int(5.6))
print(float(6))

list_batki = [2, 3, 4.6, 5, "xin chao"]
"""
index: 0 -> n-1 (n la so phan tu)
"""
print("IN ra phan tu so {}: {}".format(3, list_batki[2]))
print("IN ra phan tu so {}: {}".format(5, list_batki[4]))
print("IN ra phan tu so {}: {}".format(5, list_batki[-1]))
# int a = 5;
# int a[4] = {2, 3, 4, 7}

print(list_batki)

range_a = range(2, 9) # [2, 3, 4, 5, 6, 7, 8]
# print(range_a)

# n = int(input("Nhap vao so n: "))

# if(n in list_batki):
#     print("So {} co trong list_batki".format(n))

list_batki.append("byebye")
print(list_batki)
print(list_batki.count(2))