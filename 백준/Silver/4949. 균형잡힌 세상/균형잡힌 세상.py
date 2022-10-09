import sys

while True:
    n=input()
    stack=[]
    if n=='.':
        break
    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif not stack:
                stack.append(i)
                break
            elif stack and stack[-1] == '[':
                stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            elif not stack:
                stack.append(i)
                break
            elif stack and stack[-1] == '(':
                stack.append(i)
    if stack:
        print('no')
    else:
        print('yes')