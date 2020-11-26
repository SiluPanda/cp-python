class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a 
        return self.gcd(b, a%b)

    def hasGroupsSizeX(self, deck):
        F = {}
        N = len(deck)
        if N < 2:
            return False
        for i in range(len(deck)):
            if deck[i] in F:
                F[deck[i]] += 1
            else:
                F[deck[i]] = 1
        
        arr = list(F.values())
        ret = arr[0]
        for i in range(len(arr)):
            ret = self.gcd(ret, arr[i])
        return ret >= 2


sol = Solution()
deck = [int(s) for s in input().split()]
print(sol.hasGroupsSizeX(deck))