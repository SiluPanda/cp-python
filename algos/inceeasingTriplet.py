class Solution:
    def increasingTriplet(self, nums):
        N = len(nums)
        if N < 3:
            return False
        max_right = [0 for i in range(N)]
        max_right[N-1] = nums[N-1]
        for i in range(N-2, -1, -1):
            max_right[i] = max(max_right[i+1], nums[i])
        min_so_far = nums[0]
        for i in range(1, N-1):
            if nums[i] > min_so_far and nums[i] < max_right[i+1]:
                return True
            min_so_far = min(min_so_far, nums[i])
        return False


sol = Solution()
nums = [int(s) for s in input().split()]
print(sol.increasingTriplet(nums))
