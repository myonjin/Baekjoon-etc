import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M= map(int,sys.stdin.readline().split())
input=sys.stdin.readline

def bfs(N,M):
    visited[N]=1
    q=deque()
    q.append(N)
    while q:
        t=q.popleft()
        for i in [t-1,t+1,t*2]:
            if i==M:
                return visited[t]
            if 0<i<=100000 and visited[i]==0:
                visited[i]= visited[t] + 1
                q.append(i)


N,M = map(int,input().split())
visited=[0]*100001
if N==M:
    print(0)
else:

    print(bfs(N,M))


# print(list(combinations(arr,3)))
# print(int(s/n))