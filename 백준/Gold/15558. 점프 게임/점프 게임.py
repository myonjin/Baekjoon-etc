from collections import deque
N, K = map(int,input().split())
arr_left = list(map(int,input()))
arr_right = list(map(int,input()))

arr = [ arr_left, arr_right ]
visited = [ [False]*(N+K+1) for _ in range(2)]
x = [1,-1,K]
q = deque()
q.append([0,0,0]) # 인덱스 , 왼쪽[0]오른쪽[1] , 시간
visited[0][0] = True

def bfs():
    while q:
        i,d,t = q.popleft()
        for j in range(3):
            dx = i + x[j]

            if dx>= N:
                print(1)
                return 0


            if t < dx and arr[d][dx] == 1 and j != 2:
                if not visited[d][dx]:
                    visited[d][dx] = True
                    q.append([dx,d,t+1])

            elif t < dx and arr[1-d][dx] == 1 and not visited[1-d][dx] and j == 2:
                visited[1-d][dx] = True
                q.append([dx,1-d,t+1])
    print(0)
bfs()


