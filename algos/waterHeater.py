NW = [int(s) for s in input().split()]
N, W = NW[0], NW[1]
diff = [0 for i in range(200002)]
for _ in range(N):
    stp = [int(s) for s in input().split()]
    s, t, p = stp[0], stp[1], stp[2]
    diff[s] += p 
    diff[t] -= p
tot = [0 for i in range(200002)]
tot[0] = diff[0]
for i in range(1, 200002):
    tot[i] = tot[i-1] + diff[i]
if max(tot) <= W:
    print("Yes")
else:
    print("No")