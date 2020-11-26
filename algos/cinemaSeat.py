class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        N = len(reservedSeats)
        F = {}
        for i in range(N):
            if reservedSeats[i][0] in F:
                F[reservedSeats[i][0]].append(reservedSeats[i][1]-1)
            else:
                F[reservedSeats[i][0]] = [reservedSeats[i][1]-1]
        
        ret = 0
        
        for key in F.keys():
            reserved = F[key]
        
            '''
            attempt the first split seating, if present, try second split, if both fails, try center
            '''
            split = False

            first_split = True
            for seat in [1,2,3,4]:
                if seat in reserved:
                    first_split = False
                    break
            if first_split:
                split = True
                ret += 1

            second_split = True
            for seat in [5,6,7,8]:
                if seat in reserved:
                    second_split = False
                    break
            if second_split:
                split = True
                ret += 1

            if split == False:
                mid = True
                for seat in [3,4,5,6]:
                    if seat in reserved:
                        mid = False
                if mid:
                    ret += 1
            
        return ret + (n-len(F)) * 2
            



sol = Solution()
n = int(input())
test = int(input())
reservedSeats = []
for _ in range(N):
    row = [int(s) for s in input().split()]
    reservedSeats.append(row)
print(sol.maxNumberOfFamilies(n, reservedSeats))
