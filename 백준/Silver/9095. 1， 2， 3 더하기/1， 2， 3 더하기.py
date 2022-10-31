import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
T=int(input())
for _ in range(T):
    N= int(sys.stdin.readline())
    arr=[0]*(N+1)
    if N>0:
        arr[1]=1
    if N>1:
        arr[2]=2
    if N>2:
        arr[3]=4
    for i in range(4,N+1):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]

    print(arr[N])