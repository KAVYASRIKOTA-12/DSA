#monotonic stacks 2 types:increasing order,decreasing order
#ex:stock markets,cricket score

#monotonic increasing stack
'''arr=list(map(int,input("Enter elements: ").split()))
stack=[]
for i in arr:
    while stack and stack[-1]>i:
        stack.pop()
    stack.append(i)
print(*stack)'''

#monotonic decreasing stack
'''arr=list(map(int,input("Enter elements: ").split()))
stack=[]
for i in arr:
    while stack and stack[-1]<i:
        stack.pop()
    stack.append(i)
print(*stack)'''

#bi-tonic increasing order
#method 1
'''arr=list(map(int,input("Enter elements: ").split()))
stack=[]
stack.append(arr[1])
stack.append(arr[3])
for i in range(0,len(arr),2):
    print(arr[i],end=' ')
while stack:
    print(stack.pop(),end=' ')'''


#method 2
'''arr=list(map(int,input("Enter elements: ").split()))
stack=[]
for i in range(0,len(arr),2):
    print(arr[i],end=' ')
for i in range(1,len(arr),1):
    stack.append(arr[i])
while stack:
    print(stack.pop(),end=' ')'''


