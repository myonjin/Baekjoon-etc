from collections import deque
S = int(input())
visited = [ [False for _ in range(2002)] for _ in range(2002)]
q = deque()
q.append([1,0])
visited[1][0] = 0
def bfs(S):
    while q:
        screen, clip = q.popleft()
        if screen == S:
            return visited[screen][clip]
        if 0<=screen<10001 and not visited[screen][screen]:
            q.append([screen,screen])
            visited[screen][screen] = visited[screen][clip] + 1
        if 0<=screen<1001 and 0<=clip<1001 and not visited[screen+clip][clip]:
            q.append([screen+clip,clip])
            visited[screen+clip][clip] = visited[screen][clip] +1
        if 0<screen<1001 and 0<=clip<1001 and not visited[screen-1][clip]:
            q.append([screen-1,clip])
            visited[screen-1][clip] = visited[screen][clip] + 1
print(bfs(S))