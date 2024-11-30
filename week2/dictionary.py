# Tu dien
"""
key: unique,
value: 

Example:
- key:    value
"hello": "xin chao",
"unique": "duy nhat",
"play": ["choi (v)", "san khau(n)"]

"""

# Database users
account = {"congdaik": "absc2#!", 
           "vientoctj": "abc123", 
           "snowkool": "abc123"}
# account = key: ["congdaik", "vientoctj", "snowkool"]

username = str(input("Username: "))
password = str(input("Password: "))

if(username not in account):
    # Kiem tra username co trong tu dien hay ko, (chi kiem tra key!)
    print("Username is not existed!")
    print("Create new account: ")
    username = str(input("Username: "))
    password = str(input("Password: "))
    # Cap nhat / them thong tin cho tu dien
    account.update({username: password})
    # print(account)
else:
    if(password == account[username]):
        # account[username] : truy xuat gia tri tuong ung voi key
        print("Login is successfully!")
    else:
        print("Wrong password!")