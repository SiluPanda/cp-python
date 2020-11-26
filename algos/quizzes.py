nx = [int(s) for s in input().split()]
n, x = nx[0], nx[1]
s = input()
for i in range(len(s)):
    if s[i] != 'x':
        x += 1
    else:
        if x > 0:
            x -= 1
print(x)