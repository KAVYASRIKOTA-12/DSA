#target sum using 2 pointer approach
'''arr=list(map(int,input("enter elements: ").split()))
target=int(input("enter target:"))
arr.sort()
left=0
right=len(arr)-1
while left <right:
    total=arr[left]+arr[right]
    if total==target:
        print("pair found at",left,right)
        print("pair found are",arr[left],arr[right])
        break
    elif total<target:
        left+=1
    else:
        right-=1
else:
    print("no pair found")'''


'''arr = list(map(int, input('Enter elements: ').split()))
target = int(input('Enter target: '))
found = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print('Pair found at index', i, j)
            print('Pair found is', arr[i], arr[j])
            found = True
            break
    if found:
        break
if not found:
    print('No pair found')'''

#move all the zeroes to the last using 2 pointer approach one side
#[0,1,0,3,0,2]->[1,3,2,0,0,0]
'''arr=list(map(int,input("enter elements:").split()))
slow=0
fast=0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow],arr[fast]=arr[fast],arr[slow]
        slow+=1
print(arr)'''

#removing all zeroes
'''arr=list(map(int,input("enter elements:").split()))
for i in arr.copy():
    if i==0:
        arr.remove(i)
print(arr)'''       

#prefix sum
'''arr=list(map(int,input("enter elements:").split()))
prefix=[0]*len(arr)
print(prefix)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)'''

#display sum of given range
'''arr=list(map(int,input("enter elements:").split()))
prefix=[0]*len(arr)
print(prefix)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)
start=int(input("Give start:"))
end=int(input("Give end:"))
if start==0:
    result=prefix[end]
else:
    result=prefix[end]-prefix[start-1]
print("Range sum",result)'''

#2 sum
'''arr = list(map(int, input('Enter elements: ').split()))
target = int(input('Enter target: '))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("pair at index:",i,j)
            print("pair values:",arr[i],arr[j])
            break'''

#sliding sum / subarray sum
'''arr = list(map(int, input('Enter elements: ').split()))
k=int(input("enter slide: "))
windowsum=sum(arr[:k])
maxsum=windowsum
for i in range(k,len(arr)):
    windowsum=windowsum-arr[i-k]+arr[i]
    if windowsum>maxsum:
        maxsum=windowsum
print(maxsum)'''




