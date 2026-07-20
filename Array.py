#Reverse an array without slicing
#TC-O(n/2),SC-O(1)
arr=list(map(int,input("Enter numbers:").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("reversed array",*arr)

#left rotate an array by one (1 2 3 4 5->2 3 4 5 1)(clock wise)
#TC-O(n),SC-O(1)
arr=list(map(int,input("Enter values:").split()))
temp=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=temp
print(*arr)

#right rotate an array by one (1 2 3 4 5->5 1 2 3 4)(anti-clock wise)
arr=list(map(int,input("Enter values:").split()))
temp=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=temp
print(*arr)

#find the max element in an array 4 9 2 7->max=9
arr=list(map(int,input("Enter values:").split()))
max=arr[0]
for i in range(1,len(arr)-1):
    if arr[i]>max:
        max=arr[i]
print("Max value:",max)

#find the min element in an array 4 9 2 7->min=2
arr=list(map(int,input("Enter values:").split()))
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min=arr[i]
print("Min value:",min)



