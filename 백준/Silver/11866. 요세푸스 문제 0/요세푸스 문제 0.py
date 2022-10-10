import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
# T=int(input())
N,K = map(int,sys.stdin.readline().split())
arr=deque()
for i in range(1,N+1):
    arr.append(i)

print('<',end='')
while arr:
    arr.rotate(-(K-1))
    # print(arr)
    s=arr.popleft()
    if arr:
        print(s,end=', ')
    else:
        print(s,end='>')
