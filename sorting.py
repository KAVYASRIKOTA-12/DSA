#bubble sort
#TC-O(n),SC-O(n^2)
'''arr=list(map(int,input("Enter the values:").split()))
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)'''         

#selection sort
'''arr=list(map(int,input("Enter the values:").split()))
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j  
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(*arr)'''          

#insertion sort
'''arr=list(map(int,input("Enter values:").split()))
n=len(arr)
for i in range(1,n):
    x=arr[i]
    j=i-1
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=x    
print(*arr)'''



