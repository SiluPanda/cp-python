class Solution:
    def is_balanced(self, s):
        N = len(s)
        T = []
        for i in range(N):
            if len(T) == 0 or s[i] == '(':
                T.append(s[i])
            else:
                if s[i] == ')':
                    if len(T) and T[-1] == '(':
                        T.pop()
                    else:
                        return False
        return len(T) == 0

    def generate(self, curr_string, ret, n):
        if len(curr_string) == 2 * n:
            ret.append(curr_string)
            return
        
        self.generate(curr_string + '(', ret, n)
        self.generate(curr_string + ')', ret, n)
        
    def generateParenthesis(self, n):
        ret = []
        arr = []
        self.generate("", arr, n)
        for x in arr:
            if self.is_balanced(x):
                ret.append(x)
        return ret


sol = Solution()
n = int(input())
print(sol.generateParenthesis(n))