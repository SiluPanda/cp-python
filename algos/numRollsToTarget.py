class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 1000000007
        dp = [[0 for j in range(f + 1)] for i in range(d+1)]
        for i in range(1, d+1):
            for j in range(1, f+1):
                if 


sol = Solution()
d = int(input())
f = int(input())
target = int(input())
print(sol.numRollsToTarget(d, f, target))