import math

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for i in range(n+1)]
        is_prime[0] = False
        if n == 0:
            return 0
        is_prime[1] = False
        for i in range(2, int(math.sqrt(n+1)) + 1):
            print(i)
            if is_prime[i]:
                for p in range(i*i, n+1, i):
                    is_prime[p] = False
        print(is_prime[:21])
        ret = 0
        for i in range(n):
            if is_prime[i]:
                ret += 1
        return ret

sol = Solution()
n = int(input())
print(sol.countPrimes(n))