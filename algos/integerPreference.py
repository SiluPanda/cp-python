ABCD = [int(s) for s in input().split()]
B = ABCD[1]
C = ABCD[2]
A = ABCD[0]
D = ABCD[3]
if (A >= C and A <= D) or (B >= C and B <= D) or (C >= A and A <= B) and (D >= A and D <= B):
    print('Yes')
else:
  print('No')