def same_line(A, B, C):
    if A[0] == 0 and B[0] == 0 and C[0] == 0:
        return True
    return (C[1]-B[1]) * (B[0] - A[0]) == (C[0]-B[0]) * (B[1]-A[1])
N = int(input())
points = []
for i in range(N):
    row = [int(s) for s in input().split()]
    points.append(row)
found = False
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if same_line(points[i], points[j], points[k]):
                found = True
               
                print("Yes")
                break
        if found:
            break
    if found:
        break

if not found:
    print("No")