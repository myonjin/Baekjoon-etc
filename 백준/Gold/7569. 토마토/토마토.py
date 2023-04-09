import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())

M,N,H = map(int,input().split())
Box = [[] for _ in range(H)]
li = [[0]*M for _ in range(N)]
visited = [ [ [0 for _ in range(M)] for _ in range(N)] for _ in range(H)]


for h in range(H):
    for n in range(N):
        Box[h].append(list(map(int,sys.stdin.readline().split())))

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if Box[h][n][m] == 1:
                q.append([h,n,m])
                visited[h][n][m] = 1

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

while q:
    h,n,m = q.popleft()
    for i in range(6):
        z = h + dz[i]
        y = n + dy[i]
        x = m + dx[i]
        if 0<=z<H and 0<=y<N and 0<=x<M and Box[z][y][x] == 0 and visited[z][y][x] == 0:
            q.append([z,y,x])
            Box[z][y][x] = 1
            visited[z][y][x] = visited[h][n][m] + 1

# print(visited)
# print(Box)
result=0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if Box[h][n][m] == 0 :
                print(-1)
                exit(0)
        result=max(max(visited[h][n]),result)
print(result-1)
