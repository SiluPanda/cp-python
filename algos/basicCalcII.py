class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        stack = []
        i = 0
        tokens = []
        j = 0
        while j < N:
            if s[j].isdigit():
                k = j
                num = ""
                while k < N and s[k].isdigit():
                    num += s[k]
                    k += 1
                j = k
                tokens.append(int(num))
            elif s[j] in ['+', '-', '*', '/']:
                tokens.append(s[j])
                j += 1
            else:
                j += 1

        stack = []
        while i < len(tokens):
            if tokens[i] in ['/', '*']:
                prev = stack.pop()
                if tokens[i] == '/':
                    stack.append(prev // tokens[i+1])
                else:
                    stack.append(prev * tokens[i+1])
                i += 1
            else:
                stack.append(tokens[i])
            i += 1
        ret = 0
        for p in range(len(stack)):
            if p == 0:
                ret += stack[p]
            else:
                if stack[p] not in ['+', '-']:
                    if stack[p-1] == '+':
                        ret += stack[p]
                    else:
                        ret -= stack[p]
        return ret


sol = Solution()
s = input()
print(sol.calculate(s))