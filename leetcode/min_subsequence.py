nums = [4,3,10,9,8]
# nums = [4,4,7,6,7]
nums=[6]
a = list(sorted(nums, key=lambda x: -x))
i = 0
while sum(a[:i]) <= sum(a[i:]):
    i += 1
print(a[:i])