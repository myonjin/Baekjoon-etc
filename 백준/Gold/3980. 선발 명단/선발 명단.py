T = int(input())
def dfs(i,sum,arr,visited):
    global result
    if i == 11:
        if sum>result:
            result=sum
        return 0
    for j in range(11):
        if arr[i][j] != 0 and visited[j]==0:
            sum +=arr[i][j]
            visited[j] = 1
            dfs(i+1,sum,arr,visited)
            sum -=arr[i][j]
            visited[j] = 0


for _ in range(T):
    arr = [ list(map(int,input().split())) for _ in range(11)]
    visited = [0]*11
    result=0
    dfs(0,0,arr,visited)
    print(result)