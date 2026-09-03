#heap tree with heapify:
#packages:-
#import heapq
#heapq.heappush()-insert
#heapq.heappop()-delete
#heapq.heappushpop()-insert/delete at same time
#heapq.heapreplace()-pop smallest then push
#heapq.heapify()-
#heapq.nsmallest(2)-2 4 6 8 10-> 2 4
#heapq.nlargest(2)-2 4 6 8 10-> 8 10
#heapq.merge()-merge sorted iterables 


#heapify
'''import heapq
arr=list(map(int,input("enter elements:").split()))
heapq.heapify(arr)
print(arr)'''

#heappush
'''import heapq
arr=list(map(int,input("enter elements:").split()))
heapq.heapify(arr)
print(arr)
heapq.heappush(arr,0)
heapq.heapify(arr)'''

#heappop
'''import heapq
arr=list(map(int,input("enter elements:").split()))
heapq.heapify(arr)
print(arr)
X=heapq.heappop(arr)
print(X)
print(arr)'''

#heappushpop
'''import heapq
arr=list(map(int,input("enter elements:").split()))
x=heapq.heappushpop(arr,3)
print("Removed:",x)
print("heap",arr)
heapq.heapify(arr)
print(arr)'''

#heapreplace
'''import heapq
arr=list(map(int,input("enter elements:").split()))
y=heapq.heapreplace(arr,10)
print("Removed:",y)
print("heap",arr)'''


#nsmallest
'''import heapq
arr=list(map(int,input("enter elements:").split()))
z=heapq.nsmallest(2,arr)
print(z)'''

#nlargest
'''import heapq
arr=list(map(int,input("enter elements:").split()))
z=heapq.nlargest(2,arr)
print(z)'''

#merge
'''import heapq
arr1=list(map(int,input("enter elements:").split()))
arr2=list(map(int,input("enter elements:").split()))
arr3=list(map(int,input("enter elements:").split()))
output=heapq.merge(arr1,arr2,arr3)
print(list(output))'''

#manual code of using push
'''import heapq
heap=list(map(int,input("enter elements:").split()))
value=int(input("Enter the value to push:"))
heap.append(value)
l=len(heap)-1
while l>0:
    root=(l-1)//2
    if heap[root]<=heap[1]:
        break
    heap[root],heap[l]=heap[1],heap[root]
    l=root
print(heap)'''

#another method
'''heap = list(map(int, input('Enter elements: ').split()))
value = int(input('Enter value to push: '))

# Build min heap manually
for i in range(1, len(heap)):
    l = i

    while l > 0:
        root = (l - 1) // 2

        if heap[root] <= heap[l]:
            break

        heap[root], heap[l] = heap[l], heap[root]
        l = root

# Insert new value
heap.append(value)

l = len(heap) - 1

# Heapify up
while l > 0:
    root = (l - 1) // 2

    if heap[root] <= heap[l]:
        break

    heap[root], heap[l] = heap[l], heap[root]
    l = root

print(heap)'''

#manual code of using pop
'''import heapq
heap=list(map(int,input("enter elements:").split()))
removed=heap[0]
heap[0]=heap[-1]
heap.pop()
i=0
n=len(heap)
while True:
    left=2*i+1
    right=2*i+2
    smallest=i
    if left<n and heap[left]<heap[smallest]:
        smallest=left
    if right<n and heap[right]<heap[smallest]:
        smallest=right
    if smallest==i:
        break
    heap[i],heap[smallest]=heap[smallest],heap[i]
    i=smallest
print("Removed:",removed)
print("heap",heap)'''

#another method
'''heap = list(map(int, input('Enter elements: ').split()))
# Build min heap manually
for i in range(1, len(heap)):
    l = i
    while l > 0:
        root = (l - 1) // 2
        if heap[root] <= heap[l]:
            break
        heap[root], heap[l] = heap[l], heap[root]
        l = root
print('Min heap:', heap)
# Pop root
popped = heap[0]
# Move last element to root
heap[0] = heap[-1]
# Remove last element
heap.pop()
# Heapify down
i = 0
while True:
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    if smallest == i:
        break
    heap[i], heap[smallest] = heap[smallest], heap[i]
    i = smallest
print('Popped element:', popped)
print('Heap after pop:', heap)'''

#manual code of using replace






