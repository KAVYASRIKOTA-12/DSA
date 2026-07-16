#arg pass - return value
#TC-O(1),SC-O(1)
'''def summate(a,b):
    return a+b
num1=int(input("Enter value:"))
num2=int(input("Enter value:"))
result= summate(num1,num2)
print("Sum:",result)'''

#arg pass - no return value
#TC-O(1),SC-O(1)
'''def summate(a,b):
    print("Sum:",a+b)
num1=int(input("Enter value:"))
num2=int(input("Enter value:"))
summate(num1,num2)'''


#no arg - return value
#TC-O(1),SC-O(1)
'''def summate():
    num1=int(input("Enter value:"))
    num2=int(input("Enter value:"))
    return num1+num2
print("Sum:",summate())'''


#no arg - no return value
#TC-O(1),SC-O(1)
'''def summate():
    num1=int(input("Enter value:"))
    num2=int(input("Enter value:"))
    print("Sum:",num1+num2)
summate()'''


#direct recursion
#TC-O(n),SC-O(n)
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("Enter a value:"))
print(fact(n))'''

#indirect recursion-checking even or odd without %
#TC-O(n+1),SC-O(n)
'''def even(n):
    if n==0:
        return True
    return odd(n-1)
def odd(n):
    if n==0:
        return False
    return even(n-1)
n=int(input("Enter a value:"))
print(even(n))'''

#tail recursion
def num(n):
    if n==0:
        return
    print(n,end='-')
    num(n-1)
n=int(input("Enter a value:"))
num(n)




