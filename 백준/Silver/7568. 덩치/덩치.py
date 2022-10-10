import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
arr=[]
for _ in range(T):
    x,y = map(int,sys.stdin.readline().split())
    arr.append([x,y])
# print(arr)
for i in range(T):
    cnt=len(arr)
    for j in range(T):
        if i==j:
            continue
        if arr[i][0] >= arr[j][0] or arr[i][1] >= arr[j][1]:
            cnt-=1
    print(cnt,end=' ')
