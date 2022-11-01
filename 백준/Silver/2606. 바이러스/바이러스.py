import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
arr=[[] for _ in range(N+1)]
visited=[0]*(N+1)
q=deque()
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

q.append(1)
while q:
    p=q.popleft()
    visited[p]=1
    for i in arr[p]:
        if visited[i]==0:
            visited[i]=1
            q.append(i)
print(sum(visited)-1)

