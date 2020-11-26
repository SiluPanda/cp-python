def is_valid(new_string):
    M = len(new_string)
    if M <= 1:
        return False
    even = new_string[0]
    odd = new_string[1]
    if even == odd:
        return False
    for i in range(M):
        if (i%2 == 0 and new_string[i] != even) or (i%2 != 0 and  new_string[i] != odd):
            return False
    return True

def alternate(N, s):
    present = [False for i in range(26)]
    if N <= 1:
        return 0
    for i in range(N):
        present[ord(s[i])-97] = True
    chars = []
    ret = 0
    for i in range(26):
        if present[i]:
            chars.append(chr(i+97))
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            #build string with only chars[i] and chars[j]
            chars_to_keep = [chars[i], chars[j]]
            new_string = ""
            for k in range(N):
                if s[k] in  chars_to_keep:
                    new_string += s[k]
            if is_valid(new_string):
                ret = max(ret, len(new_string))
    return ret
            
    

N = int(input())
s = input()
print(alternate(N, s))