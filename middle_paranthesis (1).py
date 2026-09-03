exp=input('Enter an expression: ')
stack2=[]
open=0
close=0
count=0
stack3=[]
for i in exp:
    if i=='(':
        open+=1
    elif i==')':
        close+=1
if open<close:
    for ch in exp:
        count+=1
        if ch==')' and close-open==1 and stack2[count-4]!='(':
            for i in range(3,0,-1):
                stack3.append(stack2[count-i])
            temp_stack=[]
            for _ in range(4):
                temp_stack.append(stack2.pop())
                stack2.append('(')
                while temp_stack:
                    stack2.append(temp_stack.pop())
                break
            break
    print(*stack2)
else:
    print('Given expression is balanced',exp)