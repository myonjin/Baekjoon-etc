from collections import deque
K = int(input())
def bfs(start):
    q = deque([start])
    color[start] = 1
    visited[start] = True
    while q:
        s = q.popleft()

        for node in graph[s]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                color[node] = -color[s]
            elif color[node] == color[s]:
                return True
    return False



for t in range(K):
    V,E = map(int,input().split())
    graph = [ [] for _ in range(V+1)]
    visited = [False] * (V+1)
    color = [0]*(V+1)
    for g in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if not visited[i]:
            result = bfs(i)
            if result:
                print("NO")
                # print(graph)
                # print(color)
                break
    else:
        print("YES")


