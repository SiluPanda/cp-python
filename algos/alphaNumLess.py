def tokenize(s1):
    N = len(s1)
    i = 0
    curr = ""
    A = []
    while i < N:
        if s1[i].isalpha():
            j = i
            while j < N and s1[j].isalpha():
                j += 1
            A.append(s1[i:j])
            i = j
        else:
            j = i
            while j < N and s1[j].isdigit():
                j += 1
            A.append(s1[i:j])
            i = j
    return A


def alphanumericLess(s1, s2):
    A = tokenize(s1)
    B = tokenize(s2)
    
    i = 0
    j = 0
    
    N = len(A)
    M = len(B) 
    
    while i < N and j < M:
        if A[i][0].isdigit() and B[j][0].isalpha():
            return not False
        elif A[i][0].isalpha() and B[j][0].isdigit():
            return not True
        else:
            if A[i][0].isdigit():
                if int(A[i]) > int(B[j]):
                    return not True
                elif int(A[i]) < int(B[j]):
                    return not False
                else:
                    i += 1
                    j += 1
            else:
                if A[i] == B[j]:
                    i += 1
                    j += 1
                elif A[i] > B[i]:
                    return not True
                else:
                    return not False
    if i != N:
        return not True
    if j != M:
        return not False
    x = 0
    y = 0
    for p in range(len(s1)):
        x += s1[p] == '0'
    for p in range(len(s2)):
        y += s2[p] == '0'
    if x > y:
        return True
    elif x < y:
        return False
    else:
        for p in range(N):
            if A[p] != B[p]:
                an = 0
                bn = 0
                for q in range(len(A[p])):
                    an += A[p][q] == '0'
                for q in range(len(B[p])):
                    bn += B[p][q] == '0'
                return an > bn
    return False
        

s1 = input()
s2 = input()
print(alphanumericLess(s1, s2))