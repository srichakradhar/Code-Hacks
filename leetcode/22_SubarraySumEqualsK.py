from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0
        elif len(nums) < 2:
            return nums[0]
        
        

sol = Solution()
print(sol.subarraySum([1, -2, 3], 2))