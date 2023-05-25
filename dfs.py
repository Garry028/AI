graph = {
    'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]
}

visited = set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root) # this will print the node in dfs order
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)    # recursive call

dfs(visited,graph,'A')