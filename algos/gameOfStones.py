#https://www.hackerrank.com/challenges/game-of-stones-1/problem

def helper(n, count):
    if n <= 0:
        return
    if n == 2 or n == 3 or n == 5 and count%2 == 0:
        return True

    return helper(n-2, count+1) or helper(n-3, count+1) or helper(n-5, count+1)

def gameOfStones(n):
    if helper(n, 0):
        return "First"
    return "Second"

test = int(input())
for _ in range(test):
    print(gameOfStones(int(input())))