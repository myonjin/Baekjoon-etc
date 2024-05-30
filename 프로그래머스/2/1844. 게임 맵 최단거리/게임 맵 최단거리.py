from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    visited = [ [False for _ in range(m) ] for _ in range(n) ]
    q = deque()
    q.append([0,0,1])
    visited[0][0] = True
    while q:
        i,j,cnt = q.popleft()
        # print(i,j,cnt)
        if i == n-1 and j == m-1:
            return cnt
        for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
            di,dj = i+r,j+c
            if 0<=di<n and 0<=dj<m and maps[di][dj] == 1 and visited[di][dj] == False:
                visited[di][dj] = True
                q.append([di,dj,cnt+1])
                
    return -1