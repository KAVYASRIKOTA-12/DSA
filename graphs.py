#Graphs
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v):").split()
    graph[e].append(v)
    graph[v].append(e)
print("\n Graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''


#graphs with weights
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v,w=input("Enter edge(e,v,w):").split()
    w=int(w)
    graph[e].append((v,w))
    graph[v].append((e,w))
print("\n Graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''


#graph DfS
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v):").split()
    graph[e].append(v)
    graph[v].append(e)
start=input("Enter starting vertex:")
visited=set()
def dfs(vertex):
    print("Visit:",vertex)
    visited.add(vertex)
    for adj in graph[vertex]:
        if adj not in visited:
            print(vertex,'->',adj)
            dfs(adj)
            print("Backtracking to" ,vertex)
print("\n DFS with BT")
dfs(start)            
print("\n Graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''


#graph  BFS
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v):").split()
    graph[e].append(v)
    graph[v].append(e)
start=input("Enter starting vertex:")
visited=set()
queue=[]
visited.add(start)
queue.append(start)
print("\n BFS Traversal")
while queue:
    vertex=queue.pop(0)
    print(vertex,end=" ")
    for adj in graph[vertex]:
        if adj not in visited:
            visited.add(adj)
            queue.append(adj)'''

