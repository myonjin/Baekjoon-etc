
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
N=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
# print(arr)
visited=[[0]*N for _ in range(N)]
# print(visited)

def bfs(a,b):
    count=1
    q=deque()
    q.append((a,b))
    visited[a][b]=1
    while q:
        i,j=q.popleft()
        for di,dj in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0<=di<N and 0<=dj<N and arr[di][dj]==1 and visited[di][dj]==0:
                q.append((di,dj))
                visited[di][dj]=1
                count+=1
    return count
answer=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and visited[i][j]==0:
            answer.append(bfs(i,j))
# print(answer)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
