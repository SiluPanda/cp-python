def helper(graph, curr_node, visited, curr_cost, ret):
    if sum(visited) == len(graph):
        ret.append([curr_node, curr_cost])
        return
    for i in range(n):
        if i != curr_node and visited[i] == False:
            visited[i] = True
            helper(graph, i, visited , curr_cost + graph[curr_node][i], ret)
            visited[i] = False

nk = [int(s) for s in input().split()]
n, k = nk[0], nk[1]
graph = []
for i in range(n):
    r = [int(s) for s in input().split()]
    graph.append(r)
ret = []
visited = [False for i in range(n)]
visited[0] = True
helper(graph, 0, visited, 0, ret)
ans = 0
for i in range(len(ret)):
    ans += (graph[ret[i][0]][0] + ret[i][1] == k)
print(ans)