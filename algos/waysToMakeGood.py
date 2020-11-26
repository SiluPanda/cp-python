class Solution:
    def waysToMakeFair(self, nums):
        N = len(nums)
        right_odd = [0 for i in range(N)]
        right_even = [0 for i in range(N)]
        e = 0
        o = 0
        ret = 0
        if (N-1)%2 == 0:
            right_even[N-1] = nums[N-1]
        else:
            right_odd[N-1] = nums[N-1]
        for i in range(N-2, -1, -1):
            if i%2 == 0:
                right_even[i] = right_even[i+1] + nums[i]
                right_odd[i] = right_odd[i+1]
            else:
                right_odd[i] = right_odd[i+1] + nums[i]
                right_even[i] = right_even[i+1]
        for i in range(N):
            if i%2 == 0:
                right_even[i] -= nums[i]
            else:
                right_odd[i] -= nums[i]
            ret += (right_odd[i] + e == o + right_even[i])
            if i%2 == 0:
                e += nums[i]
            else:
                o += nums[i]
        return ret
            


sol = Solution()
nums = [int(s) for s in input().split()]
print(sol.waysToMakeFair(nums))