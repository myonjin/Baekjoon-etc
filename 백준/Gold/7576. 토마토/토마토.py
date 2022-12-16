
import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
# arr=[[] for _ in range(N+1)]
# visited=[0]*(N+1)
# q=deque()

M,N = map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# print(arr)
q=deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            q.append((i,j))
visited=1
while q:
    i,j=q.popleft()
    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        if 0<=i+di<N and 0<=j+dj<M and arr[i+di][j+dj]==0:
            q.append((i+di,j+dj))
            arr[i+di][j+dj]=arr[i][j]+1
# print(arr)
result=0
for ar in arr:
    max_result=max(ar)-1
    if max_result>=result:
        result=max_result
pan=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            pan+=1
if pan:
    print(-1)
else:
        print(result)

# arr.sort()
# print(arr)



