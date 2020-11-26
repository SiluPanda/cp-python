class Solution:
    def intersect(self, A, B):
        ''' finds intersection between two lists of size 2'''
        ret = []
        if B[0] in A:
            ret.append(B[0])
        if B[1] in A:
            ret.append(B[1])
        return ret

    def minDominoRotations(self, A, B):
        ''' find min rotations '''
        N = len(A)
        curr = [A[0], B[0]]
        F, T = {}, {}
        for i in range(0, N):
            curr = self.intersect(curr, [A[i], B[i]])
            if A[i] in F.keys():
                F[A[i]] += 1
            else:
                F[A[i]] = 1

            if B[i] in T.keys():
                T[B[i]] += 1
            else:
                T[B[i]] = 1

        if len(curr) == 0:
            return -1
        elif len(curr) == 1:
            curr.append(7)
            F[7] = 0
            T[7] = 0
        return min([N-F[curr[0]], N-F[curr[1]], N-T[curr[0]], N-T[curr[1]]])
        
        

sol = Solution()
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]
print(sol.minDominoRotations(A, B))