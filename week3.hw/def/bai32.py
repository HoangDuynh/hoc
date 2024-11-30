def palindrome (str):
    if len(str) < 2:
        return True
    else:
        rev_str = str.reverse ()
        if str == rev_str:
            return True
        return False