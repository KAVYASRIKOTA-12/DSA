queue=[]
size=int(input('Enter queue size: '))
for i in range(size):
    value=int(input('Enter element: '))
    queue.append(value)
start=int(input('Enter the rotation point to start: '))
index=queue.index(start)
print('Circular queue: ',end=' ')
for i in range(size):
    print(queue[(index+i)%size],end=' ')