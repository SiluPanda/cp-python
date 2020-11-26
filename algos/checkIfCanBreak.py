class Solution:
    def helper(self, F, T): 
        for i in range(26):
            '''
            get the current character, check if this or any greater than it can be possible to find
            '''
            need = F[i]
            for j in range(i, 26):
                if T[j] < need:
                    need -= T[j]
                    T[j] = 0
                else:
                    T[j] -= need
                    need = 0
            if need != 0:
                return False
        return True
                    


    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        '''
        get the frequency of all elements in s1 and s2,
        then greedily try to assign the just next greater available char
        '''
        F = [0 for i in range(26)]
        T = [0 for i in range(26)]
        N = len(s1)
        M = len(s2)
        if N != M:
            return False
        for i in range(N):
            F[ord(s1[i])-97] += 1
        for i in range(N):
            T[ord(s2[i])-97] += 1
        
        Fdup = [x for x in F]
        Tdup = [x for x in T]
        
        return self.helper(F, T) or self.helper(Tdup, Fdup)


sol = Solution()
s1 = input()
s2 = input()
print(sol.checkIfCanBreak(s1, s2))