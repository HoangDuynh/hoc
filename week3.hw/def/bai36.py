def lngt (list):
    if not list:
        return None
    return max(list, key = len)
ex = ["duynh" , "an" , "khue" , "cong" , "minh" , "thien" , "minhcong"]
print (lngt (ex))