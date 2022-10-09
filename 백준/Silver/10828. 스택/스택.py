import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
stack=deque()
for _ in range(T):
    arr=list(sys.stdin.readline().split())
    if len(arr)>1:
        stack.append(arr[1])
    else:
        if arr[0]=='top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif arr[0]=='pop':
            if stack:
                s=stack.pop()
                print(s)
            else:
                print(-1)
        elif arr[0]=='size':
            print(len(stack))
        elif arr[0]=='empty':
            if stack:
                print(0)
            else:
                print(1)
        elif arr[0]=='top':
            if stack:
                print(stack[-1])
            else:
                print(-1)



