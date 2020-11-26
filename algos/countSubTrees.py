class Solution:
    def helper(self, tree, )

    def countSubTrees(self, n, edges, labels):
        N = len(edges)
        tree = {}
        for i in range(n):
            tree[i] = []
        for i in range(N):
            tree[edges[i][0]].append(edges[i][1])
        

sol = Solution()
n = int(input())
N = int(input())
edges = []
for _ in range(N):
    e = [int(s) for s in input().split()]
    edges.append(e)
labels = input()
print(sol.countSubTreesn, edges, labels)
