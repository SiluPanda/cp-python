N = int(input())
ret = 0
for _ in range(N):
    ab = input().split()
    a, b = int(ab[0]), int(ab[1])
    ret += (b * (b+1))//2 - (a * (a-1))//2
print(ret)
