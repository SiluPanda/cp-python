import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        N = len(equations)
        M = len(queries)
        graph = {}
        for i in range(N):
            if equations[i][0] in graph:
                graph[equations[i][0]].append([equations[i][1], values[i]])
            else:
                graph[equations[i][0]] = [[equations[i][1], values[i]]]
            if equations[i][1] in graph:
                graph[equations[i][1]].append([equations[i][0], 1/values[i]])
            else:
                graph[equations[i][1]] = [[equations[i][0], 1/values[i]]]
        print(graph)
        ret = []
        for i in range(M):
            if queries[i][0] not in graph:
                ret.append(-1)
            else:
                bfs = collections.deque()
                bfs.append(queries[i][0])
                visited = set()
                visited.add(queries[i][0])
                product = {queries[i][0] : 1}
                ans = -1
                while bfs:
                    curr = bfs.popleft()
                    if curr == queries[i][1]:
                        ans = product[curr]
                        break
                    else:
                        if curr in graph:
                            for neigh in graph[curr]:
                                if neigh[0] not in visited:
                                    visited.add(neigh[0])
                                    product[neigh[0]] = product[curr] * neigh[1]
                                    bfs.append(neigh[0])
                ret.append(ans)
            
        return ret
        


sol = Solution()
equations = []
N = int(input())
for _ in range(N):
    e = [s for s in input().split()]
    equations.append(e)
values = [float(s) for s in input().split()]
M = int(input())
queries = []
for _ in range(M):
    q = [s for s in input().split()]
    queries.append(q)
print(sol.calcEquation(equations, values, queries))