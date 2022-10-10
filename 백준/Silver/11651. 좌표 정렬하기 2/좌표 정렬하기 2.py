import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
arr=deque()
for _ in range(T):
    A,B = map(int,sys.stdin.readline().split())
    arr.append([A,B])
s=sorted(arr)
s.sort(key=lambda x:x[1])
for i in range(T):
    print(*s[i])