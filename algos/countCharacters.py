class Solution:
    def countCharacters(self, words, chars):
        F = {}
        M = len(chars)
        for i in range(M):
            if chars[i] in F:
                F[chars[i]] += 1
            else:
                F[chars[i]] = 1
        ret = 0
        for word in words:
            N = len(word)
            T = {}
            for i in range(N):
                if word[i] in T:
                    T[word[i]] += 1
                else:
                    T[word[i]] = 1
            is_good = True
            for char in T.keys():
                if (char not in F) or (F[char] < T[char]):
                    is_good = False
                    break
            if is_good:
                ret += N
        return ret
                    
            
sol = Solution()
words = [s for s in input().split(',')]
chars = input()
print(sol.countCharacters(words, chars))