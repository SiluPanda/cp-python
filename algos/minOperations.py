import math

class Solution:
    def minOperations(self, nums):
        N = len(nums)
        ret = 0
        max_ele = 0   
        for i in range(N):
            if nums[i] != 0:
                ret += 1
            if nums[i] = 1 and nums[i]%2 == 1:
                ret += 1
            max_ele = max(max_ele, nums[i])
        logval = int(math.log(max_ele, 2))
        ret += (logval + max_ele - )



sol = Solution()
nums = [int(s) for s in input().split()]
print(sol.minOperations(nums))