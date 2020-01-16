i, j = 999999, 999999
flag = 0
b_palendrom = 0
while flag < 1:
    while j > 100000:
        tmp = i * j
        if str(tmp) == str(tmp)[::-1]:
            b_palendrom = tmp
            flag = 1
            break
        j -= 1
    i -= 1
print(b_palendrom)

