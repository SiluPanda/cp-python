xypq = [int(s) for s in input().split()]
x, y, p, q = xypq[0], xypq[1], xypq[2], xypq[3]
'''
slope1 = (y) / (x-ans)  slop2 = q / (p - ans)

y * p - y * ans = q * ans - q * x
ans = (y*p + q*x) / (y + q)

'''

print((y*p + q*x)/(y + q))