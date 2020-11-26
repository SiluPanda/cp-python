class Solution:
    def updateMatrix(self, matrix):
        N = len(matrix[0])
        M = 0
        if N > 0:
            M = len(matrix)
        inf = 10000000
        ret = [[inf for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                else:
                    x = inf
                    y = inf
                    if i > 0:
                        x = ret[i-1][j]
                    if j > 0:
                        y = ret[i][j-1]
                    ret[i][j] = min([ret[i][j], x+1, y+1])

        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                x = inf
                y = inf
                if i < N-1:
                    x = ret[i+1][j]
                if j < M-1:
                    y = ret[i][j+1]
                ret[i][j] = min([ret[i][j], x+1, y+1])
        return ret


sol = Solution()
N = int(input())
matrix = []
for i in range(N):
    row = [int(s) for s in input().split()]
    matrix.append(row)
ans = sol.updateMatrix(matrix)
for x in ans:
    for y in x:
        print(y, end = ' ')
    print()
