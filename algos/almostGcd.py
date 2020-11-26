import math

N = int(input())
arr = [int(s) for s in input().split()]
max_ele = max(arr)
ans = -1
max_gcd = 0
for i in range(2, max_ele + 1):
    curr= 0
    for j in range(N):
        if arr[j] % i == 0:
            curr += 1
    if curr >= max_gcd:
        max_gcd = curr
        ans = i
print(ans)

