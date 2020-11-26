from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        '''
        try to find the longest path in the tree, the middle element(s) of that path 
        would be the answer because, those would have the min heighted trees
        '''

        #make a tree adjancy list
        tree = [[] for i in range(n)]
        M = len(edges)
        if M == 0:
            return [0]
        for i in range(M):
            tree[edges[i][0]].append(edges[i][1])
            tree[edges[i][1]].append(edges[i][0])
        
        #first bfs to find one end of the longest path
        bfs = deque()
        bfs.append(0)
        distance = [0 for i in range(n)]
        visited = [False for i in range(n)]
        visited[0] = True
        while len(bfs):
            curr_node = bfs.popleft()
            for child in tree[curr_node]:
                if not visited[child]:
                    visited[child] = True
                    bfs.append(child)
                    distance[child] = distance[curr_node] + 1
        
        first_end = -1
        max_dis = -1
        for i in range(n):
            if distance[i] > max_dis:
                max_dis = distance[i]
                first_end = i
        

        #do a dfs from first_end to get actual longest path
        dfs = []
        dfs.append(first_end)
        path = [str(first_end) for i in range(n)]
        max_length = [0 for i in range(n)]
        visited = [False for i in range(n)]
        visited[first_end] = True
        while len(dfs):
            curr_node = dfs.pop()
            for child in tree[curr_node]:
                if not visited[child]:
                    visited[child] = True
                    path[child] = path[curr_node] + '-' + str(child)
                    max_length[child] = max_length[curr_node] + 1
                    dfs.append(child)
        
        second_node = -1
        longest_length = 0
        for i in range(n):
            if longest_length < max_length[i]:
                longest_length = max_length[i]
                second_node = i
        actual_path = [int(s) for s in path[second_node].split('-')]
        p = len(actual_path)
        if p%2 == 0:
            return [actual_path[p//2-1], actual_path[p//2]]
        return [actual_path[p//2]]

        

sol = Solution()
edges = []
N = int(input())
M = int(input())
for i in range(M):
    edge = [int(s) for s in input().split(' ')]
    edges.append(edge)
print(sol.findMinHeightTrees(N, edges))

