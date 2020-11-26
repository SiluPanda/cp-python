class Solution:
    def calculate(self, s):
        #tokenize the string
        tokens = []
        i = 0
        N = len(s)
        while i < N:
            if s[i].isdigit():
                j = i
                num = ""
                while j < N and s[j].isdigit():
                    num += s[j]
                    j += 1
                tokens.append(int(num))
                i = j
            elif s[i] in ['(', ')', '+', '-']:
                tokens.append(s[i])
                i += 1
            else:
                i += 1
        print(tokens)
        i = 0
        stack = [[0, 1]]
        for i in range(len(tokens)):
            if tokens[i] == '(':
                if i > 0 and tokens[i-1] == '-':
                    stack.append([0, -1])
                else:
                    stack.append([0, 1])
            elif tokens[i] == ')':
                curr_top = stack.pop()
                curr_second = stack.pop()
                stack.append([curr_second[0] + curr_top[0] * curr_top[1], curr_second[1]])
            else:
                curr_top = stack.pop()
                if type(tokens[i]) == int:
                    if i != 0 and tokens[i-1] == '-':
                        curr_top[0] -= tokens[i]
                    else:
                        curr_top[0] += tokens[i]
                stack.append(curr_top)
            print(tokens[i], stack)
        ret = 0
        for x in stack:
            ret += x[0]
        return ret
    
sol = Solution()
s = input()
print(sol.calculate(s))    
