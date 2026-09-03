#queue data structure->linear ds which follows FIFO order
#first in first out
#enqueue-insertion-append 10 [10,20,30]- put()
#dequeue-deletion-pop(0)-get()
#peek-queue[0]
#size=len(q)-q.size()
#is empty-manual-q.empty()
#is full-manual-manual
#using queue package operations in a queue:
from queue import Queue
#using queue package operations in a queue:
from queue import Queue
'''q=Queue()
n=int(input("Enter size of Queue: "))
print("enter queue elements: ")
for i in range(n):
    q.put(int(input()))
print("List of queue elements: ",list(q.queue))
print("Element at front: ",q.queue[0])
print("Removed element: ",q.get())
print("Size of Queue: ",q.qsize())
print("Size of Queue after removing an element: ",q.qsize())'''


'''from queue import Queue
q=Queue()
n=int(input("Enter size of Queue: "))
print("enter queue elements: ")
for i in range(n):
    x=int(input("Enter value:"))
    if not q.full():
        q.put(x)
    else:
        print("Queue is full. Cannot add more elements.")
print("List of queue elements: ",list(q.queue))
if q.empty():
    print("Queue is empty.")
else:
    print("Queue is not empty.")
if q.full():
    print("Queue is full.")
else:
    print("Queue is not full.")
if not q.empty():
    print("Removed element: ",q.get())'''

'''from queue import Queue
q=Queue()
n=int(input("Enter size of Queue: "))
print("enter queue elements: ")
for i in range(n):
    x=int(input("Enter value:"))
    if not q.full():
        q.put(x)
    else:
        print("Queue is full. Cannot add more elements.")
print("List of queue elements: ",list(q.queue))
if q.empty():
    print("Queue is empty.")
else:
    print("Queue is not empty.")
if q.full():
    print("Queue is full.")
else:
    print("Queue is not full.")
if not q.empty():
    print("Removed element: ",q.get())
print("Queue:",list(q.queue))'''

'''queue=[]
n=int(input("Enter size of Queue: "))
print("enter queue elements: ")
for i in range(n):
    x=int(input("Enter value:"))    
    queue.append(x)
print("Queue:",queue)
print("Removed element:",queue.pop(0))
print("Front element:",queue[0])
print("Queue",queue)
print("Size of Queue:",len(queue))'''

#operation in a queue(is_full,is_empty):
'''queue=[]
Max=5
n=int(input("enter size of queue:"))
print("Enter queue elements:")
for i in range(n):
   if len(queue)==Max:
      print("Queue is full. Cannot add more elements. ")
      break
   x=int(input("Enter value:"))
   queue.append(x)
print("Queue:",queue)
if len(queue)==0:
   print("Queue is empty.")
else:
   print("Queue is not empty.")
if len(queue)==Max:
   print("Queue is full.")  
else:
    print("Queue is not full.")
if len(queue)==0:
   print("queue is underflow")
else:
   print("Removed element:",queue.pop(0))
print("Queue:",queue)'''





