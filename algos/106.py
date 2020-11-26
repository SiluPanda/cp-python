N = int(input())
p3 = []
p5 = []
power = 1
while True:
    curr = 3 ** power
    if curr > N:
        break
    else:
        p3.append(power)
        power += 1
power = 1
while True:
    curr = 5 ** power
    if curr > N:
        break
    else:
        p5.append(power)
        power += 1
found = False
for i in range(len(p3)):
    for j in range(len(p5)):
        if 3 ** p3[i] + 5 ** p5[j] == N:
            print(p3[i], p5[j])
            found = True
            break

    if found:
        break
if not found:
    print(-1)