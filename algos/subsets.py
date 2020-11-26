class Solution:
    def generate(self, num, size):
        ret = []
        while num > 0:
            ret.append(num % 2)
            num //= 2
        curr_size = len(ret)
        for i in range(size-curr_size):
            ret.append(0)
        return ret[::-1]

    def subsets(self, nums):
        ret = []
        N = len(nums)
        for num in range(0, 1<<N):
            dec = self.generate(num, N)
            for i in range(N):
                if dec[i] == 1:
                    ret.append(nums[i])
        return ret

sol = Solution()
nums = [int(s) for s in input().split()]
print(sol.subsets(nums))