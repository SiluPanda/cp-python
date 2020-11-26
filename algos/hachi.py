def is_possible(F, num):
    T = {}
    num = str(num)
    for i in range(len(num)):
        if num[i] not in T:
            T[num[i]] = 1
        else:
            T[num[i]] += 1
    for key in T:
        if key not in F or F[key] < T[key]:
            return False
    return True

s = input()
F = {}
for i in range(len(s)):
    if s[i] in F:
        F[s[i]] += 1
    else:
        F[s[i]] = 1
if len(s) <= 2:
    if int(s)%8 == 0 or int(s[::-1])%8== 0:
        print("Yes")
    else:
        print("No")
else:
    num = 104
    found = False
    while num < 1000:
        if is_possible(F, num):
            print("Yes")
            found = True
            break
        num += 8
    if not found:
        print("No")
