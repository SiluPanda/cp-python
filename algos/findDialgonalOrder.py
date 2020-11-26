class Solution:
    def findDiagonalOrder(self, nums):
        N = len(nums)
        ret = []
        for row_num in range(N):
            startx = row_num
            starty = 0
            while startx >= 0:
                if len(nums[startx]) > starty:
                    ret.append(nums[startx][starty])
                startx -= 1
                starty += 1
        
        for col_num in range(1, len(nums[-1])):
            startx = N-1
            starty = col_num
            while startx >= 0:
                if len(nums[startx]) > starty:
                    ret.append(nums[startx][starty])
                startx -= 1
                starty += 1

        return ret

sol = Solution()
N = int(input())
nums = []
for _ in range(N):
    row = [int(s) for s in input().split()]
    nums.append(row)
print(sol.findDiagonalOrder(nums))