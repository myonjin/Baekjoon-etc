from collections import deque
n,m = map(int,input().split())
arr=  [ list(input()) for _ in range(n)]
visited = [
    [0 for _ in range(m)] for _ in range(n)
]

q=deque()
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            q.append([i,j])
            visited[i][j] = 1
            while q:
                i,j = q.popleft()
                for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    di = i + dx
                    dj = j + dy
                    if 0<=di<n and 0<=dj<m and arr[di][dj] != 'X' and visited[di][dj] == 0:
                        visited[di][dj] = 1
                        if arr[di][dj] == 'P':
                            ans +=1
                        q.append([di,dj])

if ans==0:
    print('TT')
else:
    print(ans)

