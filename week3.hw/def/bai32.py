def palindrome (str):
    if len(str) < 2:
        return True
    else:
        rev_str = str[::-1]
        if str == rev_str:
            return True
        return False
ex = ('dad')
print (palindrome(ex))