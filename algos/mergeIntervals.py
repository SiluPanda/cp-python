class Solution:
    def merge(self, intervals):
        N = len(intervals)
        intervals.sort(key = lambda x : x[0])
        ret = []
        if N == 0:
            return ret
        curr_interval = intervals[0]
        i = 1
        while i < N:
            if curr_interval[1] >= intervals[i][0]:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
            else:
                ret.append(curr_interval)
                curr_interval = intervals[i]
            i += 1
        ret.append(curr_interval)
        return ret
        

sol = Solution()
intervals = []
N = int(input())
for _ in range(N):
    r = [int(s) for s in input().split()]
    intervals.append(r)
print(sol.merge(intervals))