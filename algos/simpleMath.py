abc = [int(s) for s in input().split()]
a, b, c = abc[0], abc[1], abc[2]
ret = (a * (a+1))//2 * (b * (b+1))//2 * (c * (c+1))//2
print(ret %  998244353)