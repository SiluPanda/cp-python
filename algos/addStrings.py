class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        N = len(num1)
        M = len(num2)
        i = N-1
        j = M-1
        carry = 0
        while i >= 0 or j >= 0:
            add = 0
            if i >= 0:
                add += int(num1[i])
            if j >= 0:
                add += int(num2[j])
            add += carry
            ret += str(add % 10)
            carry = add // 10
            i -= 1
            j -= 1
        if carry > 0:
            ret += str(carry)
        return ret[::-1]

sol = Solution()
num1 = input()
num2 = input()
print(sol.addStrings(num1, num2))
        