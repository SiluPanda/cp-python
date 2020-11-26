class Solution:
    def search(self, nums, target):
        N = len(nums)
        #find the pivot element
        low = 0
        high = N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[low]:
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] 
                    
                


sol = Solution()
nums = [int(s) for s in input().split()]
target = int(input())