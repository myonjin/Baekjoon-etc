N,M = map(int,input().split())
visited = [False] * (N+1)
arr = []
def dfs():
    if len(arr) == M:
        print(*arr)
        return 0
    for i in range(1,N+1):
        if visited[i] == True:
            continue
        arr.append(i)
        visited[i] = True
        dfs()
        arr.pop()
        visited[i] = False
dfs()