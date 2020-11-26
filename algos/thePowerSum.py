import math

def helper(arr, curr_sum, curr_index, X, ret):
    if curr_index >= len(arr):
        return
    if curr_sum == X:
        ret[0] += 1
        return 
    if curr_sum > X:
        return
    print(curr_sum, curr_index)
    for i in range(curr_index+1, len(arr)):
        helper(arr, curr_sum + arr[curr_index], i, X, ret)
        helper(arr, curr_sum, i, X, ret)


def powerSum(X, N):
    #find the max range
    max_range = int(X ** (1/N))

    arr = []
    for i in range(1, max_range+1):
        arr.append(i ** N)
    print(arr)
    ret = [0]
    helper(arr, 0, 0,  X, ret)
    return ret[0]

        

X = int(input())
N = int(input())
print(powerSum(X, N))

