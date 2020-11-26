class Solution:
    def findTargetSumWays(self, nums, S):
        #TODO
        N = len(nums)
        dp = [[0 for j in range(S+1)] for i in range(N+1)]
        for i in range(1, N+1):
            for j in range(S+1):




sol = Solution()
nums = [int(s) for s in input().split()]
S = int(input())
print(sol.findTargetSumWays(nums, S))