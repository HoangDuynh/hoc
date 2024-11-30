n = int(input("Nhập số lượng phần tử: "))

list1 = []
list2 = []

for i in range(n):
  a = int(input("Nhập phần tử thứ {} của danh sách 1: ".format(i+1)))
  list1.append(a)
  b = int(input("Nhập phần tử thứ {} của danh sách 2: ".format(i+1)))
  list2.append(b)

dict = {}
for i in range(n):
  dict[list1[i]] = list2[i]

print(dict)