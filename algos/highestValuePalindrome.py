def highestValuePalindrome(s, n, k):
    
    ret = []
    for i in range(n):
        ret.append(s[i])
    i = 0
    j = n-1
    visited = [False for i in range(n)]
    while i < j:
        if s[i] != s[j]:
            if k == 0:
                print("-1")
                return
            max_value = str(max(int(s[i]), int(s[j])))
            ret[i], ret[j] = max_value, max_value
            visited[i] = True
            k -= 1
        i += 1
        j -= 1
    i = 0
    j = n-1
    while i < j:
        if k == 0:
            break
        if ret[i] != '9':
            if visited[i]:
                if k >= 1:
                    ret[i], ret[j] = '9', '9'
                    k -= 1
            else:
                if k >= 2:
                    ret[i], ret[j] = '9', '9'
                    k -= 2
                
                
        i += 1
        j -= 1
    if n%2 != 0:
        if k > 0:
            ret[n//2] = '9'
    ans = ""
    for x in ret:
        ans += x
    print(ans)


        
            

nk = input().split()
n, k = int(nk[0]), int(nk[1])
s = input()
highestValuePalindrome(s, n, k)