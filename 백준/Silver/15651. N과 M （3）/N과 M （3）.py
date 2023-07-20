N,M = map(int,input().split())
visited = [False] * (N+1)
arr = []
def dfs(s):
    if len(arr) == M:
        print(*arr)
        return 0
    for i in range(s,N+1):
            arr.append(i)
            dfs(1)
            arr.pop()
dfs(1)