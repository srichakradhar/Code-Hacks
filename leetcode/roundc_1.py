"""
Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integers N and K. The second line contains N integers. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of K-countdowns in her array.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ K ≤ N.
1 ≤ Ai ≤ 2 × 105, for all i.

Test set 1
2 ≤ N ≤ 1000.

Test set 2
2 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 2 ≤ N ≤ 1000.
"""
t = int(input())
for i in range(t):
    count = 0
    n, k = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' ')))
    l = 0
    
    while l < len(nums):
        # print('check', nums[l])
        if nums[l] == k:
            
            while l < len(nums) - 1 and nums[l] > 0 and nums[l + 1] < nums[l]:
                l += 1
                # print('found', nums[l])
            
            if nums[l] == 1:
                count += 1
        l += 1

    print("Case #{}: {}".format(i+1, count))