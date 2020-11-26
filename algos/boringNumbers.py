def isBoring(num):
    num = str(num)
    for i in range(len(num)):
        if (i+1)%2 != int(num[i])%2:
            return False
    return True

test = int(input())
for t in range(1, test + 1):
    low, high = input().split()
    low = int(low)
    high = int(high)
    ret = 0
    for num in range(low, high+1):
        ret += isBoring(num)
    print("Case #{}: {}".format(t, ret))