def count_ptu (danh_sach, char):
    count = 0
    for c in danh_sach:
        if c == char:
            count += 1
    return count