#binary search - binary search , first ,last, count occ , search in an rotated array , integer sqrt
#intger sqrt pattern
'''#tc = log(n) sc = 0(1)
n = int(input("enter a number "))
left = 0
rigth = n   
ans = 0
while left <= rigth:
    mid = (left+rigth)//2
    if mid * mid == n:
        ans = mid
        break 
    elif mid * mid<n:
        ans = mid
        left = mid+1
    else:
        rigth = mid-1
print("intger sqrt:",ans) '''

# rotate count using binnary search pattern
'''
n = list(map(int, input("enter").split()))
left = 0
rigth = len(n)-1
while left < rigth:
    mid = (left+rigth)//2
    if n[mid]>n[rigth]:
        left = mid+1
    else:
        rigth = mid
print("rotation count",left)'''