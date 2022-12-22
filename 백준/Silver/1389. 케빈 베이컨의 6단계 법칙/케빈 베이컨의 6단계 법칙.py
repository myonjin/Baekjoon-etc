
import sys
from collections import deque
import heapq
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
# arr=[[] for _ in range(N+1)]
# visited=[0]*(N+1)
# q=deque()

# arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

N,M=map(int,sys.stdin.readline().split())
bfs=[[] for _ in range(N+1)]
# bfs=[[]]*(N+1)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    bfs[a].append(b)
    bfs[b].append(a)
# print(bfs)
result=99999999999999
people=0
for i in range(1,N+1):
    visited=[0 for _ in range(N+1)]
    q=deque()
    q.append(i)
    while q:
        now=q.popleft()
        next=bfs[now]
        for n in next:
            if visited[n]==0 and not n==i:
                q.append(n)
                visited[n]=visited[now]+1
    # print(visited,sum(visited))
    visited_sum=sum(visited)
    if result>visited_sum:
        result=visited_sum
        people=i
print(people)

