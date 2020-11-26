class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = abs(x)
        ret = []
        while x > 0:
            ret.append(x%10)
            x //= 10
        print(ret)
        return ret == ret[::-1]

sol = Solution()
x = int(input())
print(sol.isPalindrome(x))