from collections import deque
N,M = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(N)]
# print(arr)
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i,j])

while q:
    i,j = q.popleft()
    for k in range(8):
        dx = i + di[k]
        dy = j + dj[k]
        if 0<=dx<N and 0<=dy<M and arr[dx][dy] == 0:
            q.append([dx,dy])
            arr[dx][dy] = arr[i][j] + 1
print(max(map(max, arr))-1)
