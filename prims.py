from heapq import *
def prims(graph,start,parent,distance,visited):
    bag=[] # list
    # bag means where to push what to push
    heappush(bag,[0,start])
    distance[start]=0  # distance of the start will be 0
    parent[start]=-1  # parent of 1st node will be -1

    while bag:
        d,n = heappop(bag)
        # this will pop the node with smallest distance
        # if this node is not visited
        if not visited[n]:
            visited[n]=1
            # make this as visited
            # now add the childs in heap
            for cd,cn in graph[n]:
                # if previous dist is greater than current dist and not visited
                if distance[cn] > cd and not visited[cn]:
                    distance[cn] = cd   # update distance
                    parent[cn] = n  # update parent
                    heappush(bag,[cd,cn])  # push the cd and cn
    print("Node:Distance",distance)
    print("Node:Parent",parent)

# 1,2,1  -> 1-u , 2-v ,1-d
ipt = [[1,2,1],[2,3,4],[3,4,1],[4,5,2],[1,5,3],[2,5,2],[2,4,1]]
n=5 # number of nodes
graph={}
parent ={}
distance={}
visited ={}
for i in range(1,n+1):
    graph[i]=[]
    parent[i]=None  # initially no parent for any node
    distance[i]=10**8+1  # initial distance will be infinite
    visited[i]=0
# for weighted graph and weight and edge into graph
for u,v,d in ipt:
    graph[u].append((d,v))
    graph[v].append((d,u))
print ("Graph",graph)
start=1 # start node will be 1st node
prims(graph,start,parent,distance,visited)