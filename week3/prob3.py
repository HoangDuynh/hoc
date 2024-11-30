# Function : Ham

# Tinh tong hai so a va b

num1 = 4
num2 = 5
num3 = 4
num4 = 6

a = [2, 3, 4]
# ...

def sumab(a, b):
    # ... 
    return a + b

def fraction(a, b):
    return a/b

"""
Cu phap de viet ham

def tenHam():
    .....
    return (!neu co)
"""

item = 5.5

print(isinstance(item, float))

if __name__ == "__main__":
    print(sumab(num1, num2))
    print(sumab(num3, num4))
    print(sumab(a[0], a[-1]))
    fraction(num1, num2)