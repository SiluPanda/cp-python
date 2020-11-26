#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171

test = int(input())
for t in range(1, test+1):
    N = int(input())
    ret = 0
    arr = [int(s) for s in input().split()]
    curr_max = -1
    for i in range(N-1):
        if arr[i] > curr_max and arr[i] > arr[i+1]:
            ret += 1
        curr_max = max(curr_max, arr[i])
    if arr[N-1] > curr_max:
        ret += 1
    print("Case #{}: {}".format(t, ret))