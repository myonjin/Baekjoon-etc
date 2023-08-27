N,M = map(int,input().split())
visited = [ [0]*(N+1) for _ in range(N+1) ]
for _ in range(M):
    a,b = map(int,input().split())
    visited[a][b] = 1
    visited[b][a] = 1
cnt = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if j == i:
            continue
        if visited[i][j] == 1:
            continue
        for k in range(j+1,N+1):
            if k == i or j == i or j==k:
                continue
            if visited[i][k] == 1 or visited[j][k]==1:
                continue
            cnt+=1
print(cnt)
