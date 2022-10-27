import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
N= int(sys.stdin.readline())
arr=[0]*110
arr[0]=1
arr[1]=1
arr[2]=1
for i in range(101):
    arr[i+3]=arr[i]+arr[i+1]
# print(arr)
for _ in range(N):
    M=int(sys.stdin.readline())
    # print(M)
    print(arr[M-1])
