class Solution:
    def getSmallestString(self, n, k):
        if n > k:
            return '-1'
        if n == k:
            return 'a' * n
        ret = ''
        while k > n-1 + 26:
            ret += 'z'
            k -= 26
            n -= 1
        print(n)
        ret += chr(k - n+1 + 96)
        ret += 'a' * (n-1)
        print(len(ret))
        return ret[::-1]



sol = Solution()
n = int(input())
k = int(input())
print(sol.getSmallestString(n, k))