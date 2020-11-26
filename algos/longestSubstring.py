class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1:
            return k
        N = len(s)
        F = {}
        head = 0
        tail = 0
        max_len = 0
        while tail < N:
            if s[tail] not in F:
                F[s[tail]] = 1
                tail += 1
                max_len = max(tail-head, max_len)
            else:
                if F[s[tail]] < k:
                    F[s[tail]] += 1
                    tail += 1
                    max_len = max(tail-head, max_len)
                else:
                    while s[head] != s[tail]:
                        F[s[head]] -= 1
                        head += 1
                    F[s[head]] -= 1
                    head += 1
        return max_len


sol = Solution()
s = input()
k = int(input())
print(sol.longestSubstring(s, k))