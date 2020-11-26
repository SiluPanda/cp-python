class Solution:
    def coinChange(self, coins, amount):
        inf = 100000000
        dp = [inf for i in range(amount + 1)]
        dp[0] = 0
        for x in coins:
            if x <= amount:
                dp[x] = 1
        for i in range(1, amount + 1):
            for x in coins:
                if x <= i:
                    dp[i] = min(dp[i], dp[i-x]+1)
        if dp[amount] >= inf:
            return -1
        return dp[amount]

sol = Solution()
coins = [int(s) for s in input().split()]
amount = int(input())
print(sol.coinChange(coins, amount))
