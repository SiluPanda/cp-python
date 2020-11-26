#https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_seen = [-1 for i in range(26)]
        max_len = -1
        N = len(s)
        for i in range(N):
            index = ord(s[i])-ord('a')
            if last_seen[index] != -1:
                max_len = max(i - 1 - last_seen[index], max_len)
            else:
                last_seen[index] = i
        return max_len

sol = Solution()
s = input()
print(sol.maxLengthBetweenEqualCharacters(s))