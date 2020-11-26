def bisect_right(heights, n, target):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if heights[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


def solve():
    nm = input().split()
    n, m = int(nm[0]), int(nm[1])
    heights = [int(s) for s in input().split()]
    forms = [int(s) for s in input().split()]
    if n == 1:
        mini = 10000000000
        for i in range(m):
            mini = min(mini, abs(heights[0]-forms[i]))
        print(mini)
        return
    heights.sort()
   
    diffs_left, diffs_right = [], []
    i = 1
    while i < n-1:
        if len(diffs_left) == 0:
            diffs_left.append(heights[i]-heights[i-1])
        else:
            diffs_left.append(diffs_left[-1] + heights[i]-heights[i-1])
        i += 2
    i = n-1
    while i > 0:
        if (len(diffs_right)) == 0:
            diffs_right.append(heights[i]-heights[i-1])
        else:
            diffs_right.append(diffs_right[-1] + heights[i] - heights[i-1])
        i -= 2
    
   


    

    mini = 1000000000

    for i in range(m):
        idx = bisect_right(heights, n, forms[i])
        value = 0
        if idx <= 1:
            value = abs(heights[0]-forms[i]) + diffs_right[-1]
        elif idx >= n-1:
            value = diffs_left[-1] + abs(forms[i]-heights[n-1])
        
        else:
            if idx%2 == 0:
                value = diffs_left[idx//2 - 1] + diffs_right[(n - (idx+1))//2 - 1] + heights[idx]-forms[i]
            else:
                value = diffs_left[idx//2 - 1] + forms[i] - heights[idx-1] + diffs_right[(n - (idx))//2 - 1]
       
        mini = min(mini, value)
    print(mini)

solve()





