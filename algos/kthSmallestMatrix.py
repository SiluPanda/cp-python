class Solution:
    def find_sum(self, mat, pointers):
        ret = 0
        N = len(mat)
        for j in range(N):
            ret += mat[i][pointers[i]]
        return ret
    def find_min(self, mat, pointers):
        index = -1
        mini = 1000000
        N = len(mat)
        for i in range(N):
            if pointers[i] < N-1 and mini > mat[i][pointers[i] + 1]:
                mini = mat[i][pointers[i] + 1]
                index = i
        return index

    def kthSmallest(self, mat, k):
        N = len(mat)
        M = 0
        if N > 0:
            M = len(mat[0])
        for i in range(N):
            mat[i].sort()
        pointers = [0 for i in range(N)]
        ret = []
        while len(ret) < k:
            ret.append(self.find_min(mat, pointers))
            min_index = self.find_min(mat, pointers)
            pointers[min_index] += 1
        return ret[k-1]
        

sol = Solution()
N = int(input())
mat = []
for _ in range(N):
    r = [int(s) for s in input().split()]
    mat.append(r)
k = int(input())
print(sol.kthSmallest(mat, k))