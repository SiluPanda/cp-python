#https://practice.geeksforgeeks.org/problems/palindromic-array/0

def num_changes(arr):
    ret = 0
    low = 0
    high = len(arr)-1
    while low < high:
        if arr[low] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] < arr[high]:
            arr[low+1] = arr[low] + arr[low + 1]
            low += 1
            ret += 1
        else:
            arr[high-1] = arr[high] + arr[high-1]
            high -= 1
            ret += 1

    return ret


test = int(input())
for _ in range(test):
    N = int(input())
    arr = [int(s) for s in input().split()]
    print(num_changes(arr))