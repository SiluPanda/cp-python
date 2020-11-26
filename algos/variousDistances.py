N = int(input())
arr = [int(s) for s in input().split()]
print(sum([abs(x) for x in arr]), sum([x**2 for x in arr]) ** 0.5, max([abs(x) for x in arr]))