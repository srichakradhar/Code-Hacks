arr = [1,2,3]
count = 0
for i in arr:
    if i + 1 in arr:
        count += 1
print(count)