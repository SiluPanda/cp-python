class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x : x[0])
        N = len(pairs)
        dp = [1 for i in range(N)]
        for i in range(1, N):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

sol = Solution()
pairs = []
N = int(input())
for i in range(N):
    pair = [int(s) for s in input().split()]
    pairs.append(pair)
print(sol.findLongestChain(pairs))