class Solution:
    def findRepeatedDnaSequences(self, s):
        N = len(s)
        if N < 10:
            return []
        if N == 10:
            return [s]
        F = {}
        ret = set()
        ans = []
        for i in range(N-9):
            curr_string = s[i:i+10]
            if curr_string in F:
                F[curr_string].append(i)
            else:
                F[curr_string] = [i]
        for i in range(N-9):
            curr_string = s[i:i+10]
            if len(F[curr_string]) > 1 and F[curr_string][-1] - F[curr_string][0] >= 10 and curr_string not in ret:
                ret.add(curr_string)
                ans.append(curr_string)
        return ans
        

sol = Solution()
s = input()
print(sol.findRepeatedDnaSequences(s))