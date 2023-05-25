def find(graph,node):
    # means this is parent
    if graph[node] < 0:
        return node
    else:
        return find(graph,graph[node]);

def union(graph,a,b,answer):
    ta = a # original values
    tb = b # original values
    a = find(graph,a)  # find parent
    b = find(graph,b) # find parent
    # if they forms cyle
    if a==b:
        pass
    else:
        answer.append([ta,tb]) # means ta tb union is  going on
        if graph[a] < graph[b]:
            graph[a] = graph[a]+graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a]+graph[b]
            graph[a] = b

ipt = [[1,2,1],[2,3,4],[3,4,1],[4,5,2],[1,5,3],[2,5,2],[2,4,1]]
# [1,2,1] -> key,value,dist (0,1,2) indexing
n=5
answer=[]
# sort by distance
ipt = sorted(ipt,key=lambda ipt:ipt[2])
graph = [-1]*(n+1) # initially all elements will be -1
for u,v,d in ipt:
    union(graph,u,v,answer)
    # union will tell after connecting both edges cycle forms or not if yes then discard it else print
print("Edge : Edge")
for item in answer:
    print(item)