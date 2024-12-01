def count_char (str, char):
    count = 0
    for c in str:
        if c == char:
            count += 1
    return count
ex = ('guava', 'a')
print (count_char(*ex))