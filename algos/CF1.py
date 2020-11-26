nm = [int(s) for s in input().split()]
n, m = nm[0], nm[1]
arr = []
for _ in range(m):
    arr.append(int(input()))
idx = 0
arr.sort()
for i in range(1, n+1):
    if idx < m and arr[idx] == i:
        idx += 1
    else:
        print(i)