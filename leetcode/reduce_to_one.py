s = int(input().strip('"'), 2)
i = 0
while s != 1:
    if s % 2 == 0:
        s = s // 2
    else:
        s += 1
    i += 1
print(i)