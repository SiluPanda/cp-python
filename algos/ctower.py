#https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3508/
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        simulate, worst complexity = N^2, for each glass, keep min(available, 1) and pass
        on the remaining to its childs
        '''
        dp = [[0 for j in range(i)] for i in range(1, 101)]
        dp[0][0] = poured
        for i in range(len(dp)-1):
            for j in range(len(dp[i])):
                can_have = min(1, dp[i][j])
                remaining = dp[i][j] - can_have
                dp[i][j] = can_have
                if remaining > 0:
                    dp[i+1][j] += remaining/2
                    dp[i+1][j+1] += remaining/2
        for x in dp:
            for y in x:
                print(y, end = ' ')
            print()
        return dp[query_row][query_glass]




sol = Solution()
poured = int(input())
query_row = int(input())
query_glass = int(input())

print(sol.champagneTower(poured, query_row, query_glass))