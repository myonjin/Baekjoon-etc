import sys
from collections import deque

def dfs(i,j,len,visited,fin):
    global N,M,result
    # print(i,j)
    len+=1
    if fin + max_val*(5-len) <=result:
        return
    if len == 5:
        # print(fin)
        if fin >= result:
            result = fin
            return

    # fin += arr[i][j]
    else:
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            di = di + i
            dj = dj + j
            if 0<=di<N and 0<=dj<M and visited[di][dj]==0:
                if len == 3:
                    visited[di][dj]=1
                    dfs(i,j,len,visited,fin + arr[di][dj] )
                    visited[di][dj]=0
                visited[di][dj]=1
                dfs(di,dj,len,visited,fin + arr[di][dj])
                visited[di][dj]=0



N,M = map(int,input().split())
arr=[]
result=0
visited=[[0]*M for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input().split())))
max_val = max(map(max, arr))
# print(max_val)
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        len=0
        fin=0
        dfs(i,j,len,visited,fin)
        visited[i][j]=0

print(result)
