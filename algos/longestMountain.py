class Solution:
    def longestMountain(self, A):
        N = len(A)
        if N == 0:
            return 0
        left = [0 for i in range(N)]
        right = [0 for i in range(N)]
        left[0] = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        right[N-1] = 1
        for i in range(N-2, -1, -1):
            if A[i] > A[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        print(left, right)
        ret = 0
        for i in range(N):
            if right[i] > 1 and left[i] > 1:

                ret = max(ret, left[i] + right[i] - 1)
        return ret


sol = Solution()
A = [int(s) for s in input().split()]
print(sol.longestMountain(A))