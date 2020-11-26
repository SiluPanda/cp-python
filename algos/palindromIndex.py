def isPalin(new_string):
    N = len(new_string)
    for i in range(N//2):
        if new_string[i] != new_string[N-i-1]:
            return False
    return True

def palindromeIndex(s):
    N = len(s)
    i = 0
    j = N-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            #check if skipping the right char would work
            new_string = s[0:j] + s[j+1:]
            if isPalin(new_string):
                return j
            #if the above does not work, check by skipping the left
            new_string = s[0:i] + s[i+1:]
            if isPalin(new_string):
                return i
            #if both did not work, it's impossible
            return -1
    return -1



queries = int(input())
while queries > 0:
    s = input()
    print(palindromeIndex(s))
    queries -= 1