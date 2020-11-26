class Solution:
    def trimMean(self, arr):
        N = len(arr)
        remove = int(N * (1/20))
        print(N, remove)
        total_sum = 0
        arr.sort()
        for i in range(remove, N-remove):
            total_sum += arr[i]
        return total_sum / (N - 2 * remove)

sol = Solution()
arr = [int(s) for s in input().split(',')]
print(sol.trimMean(arr))

