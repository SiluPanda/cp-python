import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if minutesToDie >  minutesToTest:
            return -1
        T = minutesToTest//minutesToDie + 1
        return math.ceil(math.log(buckets, 2)/math.log(T, 2))

sol = Solution()
buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
print(sol.poorPigs(buckets, minutesToDie, minutesToTest))