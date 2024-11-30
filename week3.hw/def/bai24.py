def prime (n):
    if n < 2 :
        return ("Khong phai so nguyen to")
    elif n == 2:
        return ("So nguyen to")
    else:
        for i in range (2 , int((n+1)/2)):
            if n % i == 0:
                return ("Khong phai so nguyen to")
        return ("So nguyen to")