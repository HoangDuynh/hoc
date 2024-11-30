
s = "NguyenQUocTrieu co 10 trieu"

statistic = {"So": 0, "KyTu": 0}

for char in s: # character: ky tu,
    # print(char, end=" ")
    if char.isdigit():
        statistic["So"] += 1
    elif char.isalpha():
        statistic["KyTu"] += 1
    # else:


print(statistic)
print(" ".isalpha())
print(" ".isalpha())
# for i in [0, 2, 3, 4]
# for i in s: