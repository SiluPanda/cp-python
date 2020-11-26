test = int(input())
for t in range(1, test + 1):
    matrix = []
    N = int(input())
    for i in range(N):
        row = [int(s) for s in input().split()]
        matrix.append(row)
    max_value = -1
    for i in range(N):
        startx = i
        starty = 0
        curr = 0
        while startx < N and starty < N:
            curr += matrix[startx][starty]
            startx += 1
            starty += 1
        max_value = max(max_value, curr)
    for j in range(1, N):
        startx = 0
        starty = j
        curr = 0
        while startx < N and starty < N:
            curr += matrix[startx][starty]
            startx += 1
            starty += 1
        max_value = max(max_value, curr)
    print("Case #{}: {}".format(t, max_value))