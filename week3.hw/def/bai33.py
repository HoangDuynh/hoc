def max_number (danh_sach):
    max_n = danh_sach[0]
    for n in danh_sach:
        if n > max_n:
            max_n = n
    return max_n