import collections

visited = set()
def dfs(visited,graph,root):

    if root not in visited:
        print("Dfs is: ",root) # this will print the node in dfs order
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)    # recursive call


def bfs(graph,root):
    visited = set()
    queue = collections.deque([root])
    # popleft() removes an element from the left side of the deque and returns the value.
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for adj in graph[vertex]:
            if adj not in visited:
                queue.append(adj)
    print("Bfs is: ",visited)

graph={ 0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2] }
bfs(graph,0)
dfs(visited,graph,0)
