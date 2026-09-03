#searching in arrays
# 1.extract the index
# 2.first occurence
# 3.last occurence
# 4.count occurence
# 5.largest/smallest
# 6.pair search
# 7.missing number search [1,2,3,5]


#extract the index
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
found= False
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index:",i)
        found=True
        break
if not found:
    print("Element is not array .....")'''


#first occurence
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
index=-1
for i in range(len(arr)):
    if arr[i]==target:
        index=i
        break
if index != -1:
    print("First Occurence",index)
else:
    print("Value no in array")'''


#first repeated value
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
index=-1
count=0
for i in range(len(arr)):
    if arr[i]==target:
        count+=1
        if count==2:
            index=i
            break
if index != -1:
    print("First repeated/second occurence",index)
else:
    print("Value no in array")'''


#last occurence
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
index=-1
for i in range(len(arr)):
    if arr[i]==target:
        index=i
if index != -1:
    print("last occurence",index)
else:
    print("Value no in array")'''


#count repeating number of times
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
count=0
for i in range(len(arr)):
    if arr[i]==target:
        count+=1
print("Repeating", count ,"times")'''


#pair occurences
'''arr=list(map(int,input("Enter values: ").split()))
target=int(input("Enter element to be found: "))
found= False
for i in range(len(arr)):
    for j in range(i-1,len(arr)):
        if arr[i]+arr[j]==target:
            print("pair found at",arr[i],arr[j])
            print("pair found at index",i,j)
            found=True
            break
    if found:
        break
if not found:
    print("pair not found ......")'''


#find the missing number
'''arr=list(map(int,input("Enter values: ").split()))
n=len(arr)+1
expected=n*(n+1)//2
actual=sum(arr)
print("Missing number: ",expected -actual)'''

