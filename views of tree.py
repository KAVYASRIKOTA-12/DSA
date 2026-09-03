#views of a tree:top,bottom,left,right,boundary
#Left view of a tree
'''from collections import deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
print('Left view of the tree: ')
queue=deque([root])
while queue:
    size=len(queue)
    for i in range(size):
        node=queue.popleft()
        if i==0:
            print(node.data,end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)'''


#Top view of the tree
'''from collections import defaultdict,deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
print('Top view of the tree: ')
queue=deque([(root,0)])
top={}
while queue:
    node,column=queue.popleft()
    if column not in top:
        top[column]=node.data
    if node.left:
        queue.append((node.left,column-1)) 
    if node.right:
        queue.append((node.right,column+1)) 
print("Top view...")
for column in sorted(top):
        print(top[column],end=' ')'''


#Bottom view of the tree
'''from collections import deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
print('Bottom view of the tree: ')
queue=deque([(root,0)])
bottom={}
while queue:
    node,column=queue.popleft()
    bottom[column]=node.data
    if node.left:
        queue.append((node.left,column-1)) 
    if node.right:
        queue.append((node.right,column+1)) 
print("bottom view...")
for column in sorted(bottom):
        print(bottom[column],end=' ')'''


#Boundary view of the tree
'''from collections import deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
print('Boundary view of the tree: ')
queue=deque([(root,0)])
result=[]
result.append(root.data)
node=root.left
while node:
    if node.left or node.right:
        result.append(node.data)
    if node.left:
        node=node.left
    else:
        node=node.right  
def addleaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        result.append(node.data)
        return
    addleaves(node.left)
    addleaves(node.right)
addleaves(root)
rightboundary=[]
node=root.right
while node:
    if node.left or node.right:
        rightboundary.append(node.data)
    if node.right:
        node=node.right
    else:
        node=node.left
rightboundary.reverse()
result.extend(rightboundary)
print(*result)'''




