class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        N = len(pattern)
        words = [s for s in s.split(' ')]
        F = {}
        T = {}
        if N != len(words):
            return False
        for i in range(N):
            if pattern[i] not in F:
                F[pattern[i]] = words[i]
            else:
                if F[pattern[i]] != words[i]:
                    return False
            if words[i] not in T:
                T[words[i]] = pattern[i]
            else:
                if T[words[i]] != pattern[i]:
                    return False
        return True

pattern = input()
s = input()
sol = Solution()
print(sol.wordPattern(pattern, s))