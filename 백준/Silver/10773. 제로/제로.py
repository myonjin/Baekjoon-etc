import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
stack=deque()
for _ in range(T):
    n=int(sys.stdin.readline())
    if n==0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))

