test = int(input())
for t in range(1, test + 1):
    nks = [int(s) for s in input().split()]
    n, k, s = nks[0], nks[1], nks[2]
    ans = min(k-s+n-s+1+k-1, k-1+n+1)
    print("Case #{}: {}".format(t, ans))