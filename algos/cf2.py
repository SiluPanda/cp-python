import math

t = int(input())
for _ in range(t):
    a = [int(s) for s in input().split()]
    print(math.ceil(abs(a[1]-a[0])/a[2]))
