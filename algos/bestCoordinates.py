#https://leetcode.com/problems/coordinate-with-maximum-network-quality/

import math

class Solution:
    def distance(self, A, B):
        return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

    def bestCoordinate(self, towers, radius):
        max_x = 0
        max_y = 0
        for c in towers:
            max_x = max(max_x, c[0])
            max_y = max(max_y, c[1])
        cord = []
        max_quality = -1
        for x in range(max_x + 1 + radius):
            for y in range(max_y + 1 + radius):
                quality = 0
                for i in range(len(towers)):
                    dis = self.distance([x,y], towers[i][:2])
                    if dis <= radius:
                        quality += math.floor(towers[i][2] / (1 + dis))
                if quality > max_quality:
                    cord = [x, y]
                    max_quality = quality
        return cord

N = int(input())
towers = []
for _ in range(N):
    curr = [int(s) for s in input().split()]
    towers.append(curr)
radius = int(input())
sol = Solution()
print(sol.bestCoordinate(towers, radius))



