'''1/2!+3/4!+5/6!+...........n terms
n=10'''

#TC-O(n^2),SC-O(1)
'''n=int(input("Enter a term:"))
sum=0
i=1
for k in range(n):
    fact=1
    for j in range(1,i+2):
        fact *= j
    term=i/fact
    print(f"Term {k+1}={i}/{i+1}!={term}")
    sum+=term
    i+=2
print("Sum",sum)'''

#TC-O(n),SC-O(1)
'''import math
n=int(input("Enter a term:"))
sum=0
odd=1
even=2
for i in range(n):
    term=odd/math.factorial(even)
    print(f"Term {i+1}={odd}/{even}!={term}")
    sum+=term
    odd+=2
    even+=2
print(sum)'''

#back tracking
#TC-O(n+1),SC-O(1)
'''def print_numbers(i,n):
    if i>n:
        return
    print(i)
    print_numbers(i+1,n)
n=int(input("Enter a number:"))
print_numbers(1,n)'''

#tree recursion
#TC-O(),SC-O()
'''def tree(n):
    if n==0:
        return
    print(n)
    tree(n-1)
    tree(n-1)
n=int(input("Enter a number:"))
tree(n)'''

#fibonocci series
'''f(n)=f(n-1)+f(n-2)
0 1 1 2 3 5 8 13 21 34'''

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input("Enter a num:"))
for i in range(n):
    print(fib(i),end=' ')
    




        