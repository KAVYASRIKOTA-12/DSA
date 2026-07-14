#program to print a square pattern
'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''  

#To print hallow square
'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''
        

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if  i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n-1 or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''


'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()'''

# to print right-angle triangle
'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(i):
        print("*",end=' ')   
    print()'''


# to print inverted rightangled triangle
'''n=int(input("Enter the size: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')   
    print()'''

# to print symmetric 
n=int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')   
    for j in range(i):
        print("*",end=' ')    
    print()



