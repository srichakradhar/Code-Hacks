nums = [0,0,1]
nums = [0,1,0,3,12]
count = 0
n= len(nums)
for i in range(n):
    if nums[i] != 0:
        nums[count] = nums[i]
        count += 1
while count < n:
    nums[count] = 0
    count += 1
print(nums)