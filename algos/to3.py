N = int(input())
N = str(N)
p = 0
r = [0 for i in range(3)]
for i in range(len(N)):
    d = int(N[i])
    p += d
    r[d%3] += 1
if p%3 == 0:
    print(0)
else:
    if p%3 == 2:
        if r[2] >= 1 and len(N) > 1:
            print(1)
        elif r[1] >= 2 and len(N) > 2:
            print(2)
        else:
            print(-1)
    else:
        if (r[1] >= 1 and len(N) > 1):
            print(1)
        elif r[2] >= 2 and len(N) > 2:
            print(2)
        else:
            print(-1)
        
