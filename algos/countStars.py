def count_neighbours(graph, node):
    """
    helper function to count the number of 
    neighbours of a node in the graph
    """
    count = 0
    for i in range(len(graph[node])):
        if node != i and graph[node][i] == True:
            count += 1
    return count

def countStars(graph):
    N = len(graph)
    """
    for each node ni, if it is a star with ni as center, 
    count it as a star. if it is a star with size = 2, count it as 0.5
    as the other node will also be counted as a star
    """
    print(graph)
    ret = 0
    for i in range(N):
        possible_center = i
        num_neigh = count_neighbours(graph, possible_center)
        is_center = True
        for j in range(N):
            if graph[possible_center][j] == True and j != possible_center and count_neighbours(graph, j) != 1:
                is_center = False
                break
        print(possible_center, num_neigh, is_center)
        if num_neigh >= 1 and is_center == True and graph[i][i] != True:
            if num_neigh == 1:
                ret += 0.5
            else:
                ret += 1
    return int(ret) 

N = int(input())
graph = []
for i in range(N):
    row = [int(s) for s in input().split()]
    graph.append(row)
print(countStars(graph))
            

