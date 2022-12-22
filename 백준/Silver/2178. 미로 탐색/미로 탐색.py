
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
maze=[list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
q=deque()
q.append((0,0))
visited[0][0]=1
while q:
    s_i,s_j=q.popleft()
    for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
        di=s_i+i; dj=s_j+j;
        if 0<=di<N and 0<=dj<M and maze[di][dj]==1 and visited[di][dj]==0:
            q.append((di,dj))
            visited[di][dj]=visited[s_i][s_j]+1
print(visited[N-1][M-1])
