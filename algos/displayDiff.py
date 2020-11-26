#https://app.codesignal.com/challenge/rkM8GAzu8KNpBRGME

def lcs(X, Y, m, n): 
    ''' 
    create a matrix and store the longest common subsequence,
    then refer the table to find the actual sequence.
    Reference: https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    '''

    #table to store the longest common subsequence
    longest_table = [[0 for x in range(n+1)] for x in range(m+1)] 

    #populating the table from top to bottom
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                longest_table[i][j] = 0
            elif X[i-1] == Y[j-1]:
                longest_table[i][j] = 1 + longest_table[i-1][j-1]
            else:
                longest_table[i][j] = max(longest_table[i-1][j], longest_table[i][j-1])
    
    
    #finding the actual string from the table
    length = longest_table[m][n]
    longest_common_string = ["" for i in range(length)]
    #start from the bottom of the table
    i = m
    j = n
    while i > 0 and j > 0:
        #if the current character of both strings are same, then it is definitely present in common substring
        if X[i-1] == Y[j-1]:
            longest_common_string[length-1] = X[i-1]
            i -= 1
            j -= 1
            length -= 1
        else:
            #find the maximum direction, preference to the second string
            if longest_table[i-1][j] > longest_table[i][j-1]:
                i -= 1
            else:
                j -= 1
  
    return "".join(longest_common_string)  

def displayDiff(oldVersion, newVersion):
    N = len(oldVersion)
    M = len(newVersion)

    #find the longest common substring between two strings
    longest_sub = lcs(oldVersion, newVersion, len(oldVersion), len(newVersion))
    ret = ""

    #find and store the differences in longest common substring and old version, with the index
    #diff starts from
    i = 0
    j = 0
    diff = ""
    old_index = {}
    while i < N and j < len(longest_sub):
        if longest_sub[j] == oldVersion[i]:
            i += 1
            j += 1
        else:
            k = i
            while k < N and oldVersion[k] != longest_sub[j]:
                diff += oldVersion[k]
                k += 1
            old_index[j] = diff
            diff = ""
            i = k
    if i != N:
        old_index[j] = ""
    while i < N:
        old_index[j] += oldVersion[i]
        i += 1
    
    #find and store the differences in longest common substring and new version, with the index
    #diff starts from
    i = 0
    j = 0
    diff = ""
    new_index = {}
    while i < M and j < len(longest_sub):
        if longest_sub[j] == newVersion[i]:
            i += 1
            j += 1
        else:
            k = i
            while k < M and newVersion[k] != longest_sub[j]:
                diff += newVersion[k]
                k += 1
            new_index[j] = diff
            diff = ""
            i = k
    if i != M:
        new_index[j] = ""
    while i < M:
        new_index[j] += newVersion[i]
        i += 1
    
    #finally join the diffs in both with one string
    for i in range(len(longest_sub)):
        if i in old_index:
            ret += '(' + old_index[i] + ')'
        if i in new_index:
            ret += '[' + new_index[i] + ']'
        ret += longest_sub[i]
    if len(longest_sub) in old_index:
        ret += '(' + old_index[len(longest_sub)] + ')'
    if len(longest_sub) in new_index:
        ret += '[' + new_index[len(longest_sub)] + ']'
    
   
    return ret






oldVersion = input()
newVersion = input()

print(displayDiff(oldVersion, newVersion))
