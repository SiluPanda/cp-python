xyab = [int(s) for s in input().split()]
x, y, a, b = xyab[0], xyab[1], xyab[2], xyab[3]
ret = 0
while (a-1) * x < b:
    x *= a
    if x < y:
        ret += 1
    else:
        break
if x < y:
    if (y-x)%b == 0:
        ret += (y-x)//b - 1
    else:
        ret += (y-x)//b
print(ret)
    