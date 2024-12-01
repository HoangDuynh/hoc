def avg (list):
    if not list :
        return 0
    return ("Trung binh cong: " ,(sum(list) / len(list)))

ex = [1 , 2 , 3 , 4]
print (avg (ex))