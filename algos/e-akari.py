hwnm = [int(s) for s in input().split()]
h, w, n, m = hwnm[0], hwnm[1], hwnm[2], hwnm[3]
grid = [[0 for j in range(w)] for i in range(h)]
light = [[0 for j in range(w)] for i in range(h)]

for _ in range(n):
    xy = input().split()
    x, y = int(xy[0]), int(xy[1])
    grid[x-1][y-1] = 1
    light[x-1][y-1] = 1

for _ in range(m):
    xy = input().split()
    x, y = int(xy[0]), int(xy[1])
    grid[x-1][y-1] = -1

for i in range(h):
    for j in range(w):
        if grid[i][j] == 1:
            x, y = i-1, j
            while x >= 0 and grid[x][y] == 0:
                light[x][y] = 1
                x -= 1
            x = i+1
            while x < h and grid[x][y] == 0:
                light[x][y] = 1
                x += 1
            x = i
            y = j-1
            while y >= 0 and grid[x][y] == 0:
                light[x][y] = 1
                y -= 1
            y = j+1
            while y < w and grid[x][y] == 0:
                light[x][y] = 1
                y += 1

ret = 0
for x in light:
    ret += sum(x)
print(ret)

