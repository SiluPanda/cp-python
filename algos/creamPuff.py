N = int(input())
ret = []
for i in range(1, int(N**0.5) + 1):
    if N%i == 0:
        if N//i == i:
            ret.append(i)
        else:
            ret.extend([i, N//i])
ret.sort()
for x in ret:
    print(x)