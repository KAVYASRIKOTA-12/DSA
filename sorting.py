#bubble sort
#TC-O(n),SC-O(n^2)
arr=list(map(int,input("Enter the values:").split()))
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)      

#selection sort
arr=list(map(int,input("Enter the values:").split()))
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j  
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(*arr)    

#insertion sort
arr=list(map(int,input("Enter values:").split()))
n=len(arr)
for i in range(1,n):
    x=arr[i]
    j=i-1
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=x    
print(*arr)

#merge sort
#divide and conquer
#TC-O(nlogn),SC-O(n)
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result            
arr=list(map(int,input("Enter values:").split()))
sorted_arr=merge_sort(arr)
print(*sorted_arr)

#flip sort/pancake sort
#TC-O(n),SC-O(1)
arr=list(map(int,input("Enter elements:").split()))
def flip(arr,k):
    left=0
    right=k 
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
n=len(arr)        
for curr_size in range(n,1,-1):
    max_index=0
    for i in range(1,curr_size):
        if arr[i]>arr[max_index]:
            max_index=i
    if max_index!=curr_size-1:
        flip(arr,max_index)
        flip(arr,curr_size-1)
print(*arr)

#quick sort
#TC-O(nlogn),SC:-best &avg case-O(logn),worst case-O(n)
def part(arr,low,high):
    piv=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<piv:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        piv=part(arr,low,high)
        quick_sort(arr,low,piv-1)
        quick_sort(arr,piv+1,high)
arr=list(map(int,input("Enter elements:").split()))
quick_sort(arr,0,len(arr)-1)
print(*arr)      
