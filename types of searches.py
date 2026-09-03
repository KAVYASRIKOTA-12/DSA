#types of searchs - liner search (un/s) , binary (s) , jump (S) , interpolation (S) , exponential(s)
#binary search
'''
arr = list(map(int, input("Enter elements :").split()))
t = int(input("enter the target:"))
left = 0
rigth = len(arr)-1
while left <= rigth:
    mid = (left+rigth)//2
    if arr[mid] == t:
        print("Element found at:",mid)
        break
    elif t<arr[mid]:
        rigth=mid-1
    else:
        left += mid +1
else:
    print("element not found")  '''

#jump
'''
arr=list(map(int,input("enter the elements:").split()))
target=int(input("enter the target:"))
n=len(arr)
step=int(n**0.5)
i=0
while i<n and arr[min(i+step,n)-1]<target:
    i+=step
found=False
for j in range(i,min(i+step,n)):
    if arr[j]==target:
        print("element found at index",j)
        found=True
        break
if not found:
    print("element not in array")'''