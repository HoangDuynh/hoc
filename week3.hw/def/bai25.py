import math
def circle (r):
    if r <= 0:
        return False
    else :
        chuvi = 2 * math.pi * r
        dientich = math.pi * r**2
        return chuvi , dientich