#dijkstra's approach:

#shortest path ->where edge weight represents distance
vertices=input("Enter vertices:").split()
graph={}
for v in vertices:
    graph[v]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v,w=input("Enter edge(source,destination,distance):").split()
    w=int(w)
    graph[e].append((v,w))
    graph[v].append((e,w))
source=input("Enter source vertex:")
destination=input("Enter destination vertex:")
distance={}
previous={}
for v in vertices:
    distance[v]=float('inf')
    previous[v]=None
distance[source]=0
visited=set()
for i in range(len(vertices)):
    current=None
    minimum=float('inf')
    for v in vertices:
        if v not in visited and distance[v]<minimum:
            minimum=distance[v]
            current=v
    if current is None:
        break
    visited.add(current)
    for adj,weight in graph[current]:
        new_distance=distance[current]+weight
        if new_distance<distance[adj]:
            distance[adj]=new_distance           
            previous[adj]=current
path=[]
current=destination
while current is not None:
    path.append(current)
    current=previous[current]
path.reverse()
if distance[destination]==float('inf'):
    print("path exists")
else:
    print("\nShortest distance:",distance[destination])
    print("\nShortest path: ","->".join(path))
    































































































































