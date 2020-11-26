class Solution:
    def helper(self, curr_board, n, ret):
        if len(curr_board) == n:
            copy = []
            for i in range(n):
                copy.append(''.join(curr_board[i]))
            ret.append(copy)
            return
        for i in range(n):
            row = len(curr_board)-1
            col = i-1
            is_good = True
            for j in range(len(curr_board)):
                if curr_board[j][i] == 'Q':
                    is_good = False
                    break
            while row >= 0 and col >= 0:
                if curr_board[row][col] == 'Q':
                    is_good = False
                    break
                row -= 1
                col -= 1
            col = i+1
            row = len(curr_board)-1
            while row >= 0 and col < n:
                if curr_board[row][col] == 'Q':
                    is_good = False
                    break
                row -= 1
                col += 1
            if is_good:
                P = ['.' for j in range(n)]
                P[i] = 'Q'
                self.helper(curr_board + [P], n, ret)

               
                  
                

    def solveNQueens(self, n):
        ret = []
        self.helper([], n, ret)
        return ret

sol = Solution()
n = int(input())
print(sol.solveNQueens(n))