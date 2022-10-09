import sys
T=int(input())
for _ in range(T):
    n= input()
    stack=[]
    result='YES'
    for i in n:
        if not stack and i==')':
            result='NO'
        else:
            if i=='(':
                stack.append('(')
            elif i==')':
                stack.pop()
    if stack:
        result='NO'

    print(result)

