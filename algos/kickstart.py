def bisect(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

test = int(input())
for t in range(1, test+1):
    s = input()
    kick = []
    start = []
    N = len(s)
    for i in range(N-3):
        if s[i:i+4] == 'KICK':
            kick.append(i)
    for i in range(N-4):
        if s[i:i+5] == 'START':
            start.append(i)
    ret = 0
    for index in kick:
        ret += len(start)-bisect(start, index)
    print("Case #{}: {}".format(t, ret))