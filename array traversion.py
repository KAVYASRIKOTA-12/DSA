#TC-O(n^2),SC-O(1)
int(input("Enter the size of matrix:"))
arr = [[0]*n for _ in range(n)]
top = 0
left = 0
right = n-1
bottom = n-1
num = 1

while top <= bottom and left <= right:
    # Traverse top row (left -> right)
    for i in range(left, right+1):
        arr[top][i] = num
        num += 1
    top += 1

    # Traverse right column (top -> bottom)
    for i in range(top, bottom+1):
        arr[i][right] = num
        num += 1
    right -= 1

    # Traverse bottom row (right -> left)
    if top <= bottom:  # Add check to avoid repeating
        for i in range(right, left-1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1

    # Traverse left column (bottom -> top)
    if left <= right:  # Add check to avoid repeating
        for i in range(bottom, top-1, -1):
            arr[i][left] = num
            num += 1
        left += 1

# Print the spiral matrix
for row in arr:
    print(*row)


#another method
# Traversal of above matrix
n=int(input('Size of matrix: '))
arr=[[0]*n for _ in range(n)]
print(arr)
matrix=[]
for i in range(n):
    
    row=list(map(int,input().split()))
    matrix.append(row)
top=0
left=0
right=n-1
bottom=n-1
num=1
while left<=right and top<=bottom:
    # in top, left -> right
    for i in range(left,right+1):
        print(matrix[top][i],end='  ')
        num+=1
    top+=1
    # in right, top -> bottom
    for i in range(top,bottom+1):
        print(matrix[i][right],end='  ')
        num+=1
    right-=1
    # in bottom, right -> left
    for i in range(right,left-1,-1):
        print(matrix[bottom][i],end='  ')
        num+=1
    bottom-=1
    # in left, bottom -> top
    for i in range(bottom,top-1,-1):
        print(matrix[i][left],end='  ')
        num+=1
    left+=1
