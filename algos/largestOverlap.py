class Solution:
    def largestOverlap(self, img1, img2):
        F = {}
        T = {}
        N = len(img1)
        for i in range(N):
            for j in range(N):
                if img1[i][j] == 1:
                    if i not in F:
                       F[i] = set([j])
                    else:
                        F[i].add(j)

                if img2[i][j] == 1:
                    if i not in T:
                        T[i] = set([j])
                    else:
                        T[i].add(j)
        ret = 0
        for x in range(0, N):
            for y in range(0, N):
                count = [0, 0, 0, 0]
                for i in F:
                    for j in F[i]:
                        if i+x < N and j+y < N and i+x in T and j+y in T[i+x]:
                            count[0] += 1
                        if i-x >= 0 and j-y >= 0 and i-x in T and j-y in T[i-x]:
                            count[3] += 1
                        if i-x >= 0 and j+y < N and i-x in T and j+y in T[i-x]:
                            count[1] += 1
                        if i+x < N and j-y >= 0 and i+x in T and j-y in T[i+x]:
                            count[2] += 1

                ret = max(ret, max(count))
        return ret

n = int(input())
img1 = []
for _ in range(n):
    r = [int(s) for s in input().split()]
    img1.append(r)
img2 = []
for _ in range(n):
    r = [int(s) for s in input().split()]
    img2.append(r)
sol = Solution()
print(sol.largestOverlap(img1, img2))