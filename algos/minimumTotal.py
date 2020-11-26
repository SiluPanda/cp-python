class Solution:
    def minimumTotal(self, triangle):
        dp = []
        N = len(triangle)
        for i in range(N):
            if i == 0:
                dp.append([x for x in triangle[i]])
            else:
                curr_row = [10000000 for j in range(len(triangle[i]))]
                curr_row[0] = dp[-1][0] + triangle[i][0]
                curr_row[-1] = dp[-1][-1] + triangle[i][-1]
                for j in range(1, len(triangle[i])-1):
                    curr_row[j] = min(dp[-1][j-1], dp[-1][j]) + triangle[i][j]
                dp.append(curr_row)
        return min(dp[-1])

sol = Solution()
rows = int(input())
triangle = []
for i in range(rows):
    r = [int(s) for s in input().split()]
    triange.append(r)
print(sol.minimumTotal(triangle))