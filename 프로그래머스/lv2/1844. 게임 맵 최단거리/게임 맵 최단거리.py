from collections import deque 
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [ [0]*m for _ in range(n)]
    answer = 0
    q = deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y = q.popleft()
        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
            dx = x+i
            dy = y+j
            if 0<=dx<n and 0<=dy<m and visited[dx][dy] == 0 and maps[dx][dy] == 1:
                q.append([dx,dy])
                visited[dx][dy] = visited[x][y] + 1

                if dx == n-1 and dy == m-1:
                    return visited[dx][dy]

    return -1