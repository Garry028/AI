from heapq import *
def dijkstra (graph,start,visited,distance):
    distance[start]=0
    bag=[]
    heappush(bag,(0,start))
    while bag:
        d,n = heappop(bag)  # Node with minimum distance will pop
        visited[n]=1 # become visited
        for cd,cn in graph[n]:   # check for all adjecent node of selected node
            # if  not visited and parent dist + new distance is less than current node's dist from source
            if not visited[cn] and distance[n] + cd < distance[cn]:
                # update new distance and parent dist + new dist
                distance[cn] = distance[n] + cd
                # push new distance and node in bag
                heappush(bag,(distance[cn],cn))
    print("Vertex : Shortest Distance" ,distance)

ipt =[[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,3]]
n=5
graph ={}
distance={}
visited={}

for i in range (1,n+1):
    graph[i]=[]
    distance[i]=10**8+1  # infinite distance initially
    visited[i]=0

for u,v,d in ipt:
    graph[u].append([d,v])
    graph[v].append([d,u])

start=1 # this is source
dijkstra(graph,start,visited,distance)
