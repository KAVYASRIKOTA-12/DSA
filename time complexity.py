#here time complexity N+N=2N,space complexity O(1)
#2 loops parallelly
'''n=int(input("Enter number:"))
for i in range (n):
    print('#')
for j in range(n):
    print('$')'''



#here time complexity:O(n),space complexity:O(2)
'''n=int(input("Enter the number:"))
for i in range(n):
    print(i,i+100)'''


#here time complexity:O(1),space complexity:n^3
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k,end=" ")
        print()
    print()'''


#here time complexity:O(n),space complexity:O(n)
'''n=int(input())
arr=[]
for i in range(n):
    arr.append(i)'''


#here time complexity:Olog((N)),space complexity:O(1)
'''n=int(input())
while n>1:
    print(n)
    n//=2
print(n)'''


 #here time complexity: O(log(log(N))),space complexity:O(1)   
'''n=int(input())
while n>2:
    print(n)
    n=int(n**0.5)
print(n)'''





