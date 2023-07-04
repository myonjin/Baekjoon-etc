from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
arr = [[*map(str, input().rstrip())] for _ in range(R)]

fire_visited=[
    [0 for _ in range(C)] for _ in range(R)
]

man_visited=[
    [0 for _ in range(C)] for _ in range(R)
]
# 불 가는 시간
q = deque()
fir = []
for i in range(R):
    for j in range(C):
        vis_cnt = 1
        if arr[i][j] == 'F':
            q.append([i,j])
            fire_visited[i][j] = 1
while q:
    i,j = q.popleft()
    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        dx = i+ di
        dy = j+ dj
        if 0<= dx < R and 0<= dy <C and arr[dx][dy] !='#' and (fire_visited[dx][dy] == 0 ) :
            fire_visited[dx][dy] = fire_visited[i][j] +1
            q.append([dx,dy])

#사람이 가는 루트 ( 불 시간 보다 작아야함 )
q = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            if i == R - 1 or i == 0 or j == 0 or j == C - 1:
                print(1)
                exit()
            q.append([i,j])
            man_visited[i][j] = 1
            while q:
                i, j = q.popleft()
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    dx = i + di
                    dy = j + dj
                    if 0<= dx < R and 0<= dy <C and arr[dx][dy] != '#' and (fire_visited[dx][dy] > man_visited[i][j]+1 or fire_visited[dx][dy]==0) and man_visited[dx][dy] == 0:
                        man_visited[dx][dy] = man_visited[i][j] +1
                        if dx == R-1 or dx == 0 or dy == 0 or dy ==C-1:
                            print(man_visited[dx][dy])
                            # print(*man_visited)
                            exit()
                        q.append([dx, dy])
# print(*fire_visited)
# print(*man_visited)

print("IMPOSSIBLE")