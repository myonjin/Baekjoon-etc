import sys
from collections import deque
# from itertools import combinations
# from collections import deque
N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
arr=[[] for _ in range(N+1)]
visited=[0]*(N+1)
q=deque()
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
count=0
for i in range(1,N+1):
    q.append(i)
    if visited[i]==0:
        count+=1
    while q:
        p=q.popleft()
        visited[p]=1
        for j in arr[p]:
            if visited[j]==0:
                visited[j]=1
                q.append(j)
print(count)

# print(arr)
# print(visited)