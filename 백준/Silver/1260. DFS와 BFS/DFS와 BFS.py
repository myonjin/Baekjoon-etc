import sys
from collections import deque
N,M,V=map(int,sys.stdin.readline().split())
arr=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort(reverse=True)
# print(arr)
# dfs
visited=[0]*(N+1)
stack=deque()
stack.append(V)
while stack:
    p=stack.pop()
    if visited[p]==0:
        visited[p]=1
        print(p,end=' ')
        for i in arr[p]:
            if visited[i]==0:
                stack.append(i)
#bfs
print()
for i in arr:
    i.sort()
visited=[0]*(N+1)
que=deque()
que.append(V)
while que:
    q=que.popleft()
    if visited[q]==0:
        visited[q]=1
        print(q,end=' ')
        for i in arr[q]:
            if visited[i]==0:
                que.append(i)

# visited=[0]*(N+1)
# while stack:
#     p = stack[-1]
#     for i in arr[p]:
#         if visited[i] == 0:
#             stack.append(i)
#             break
#     else:
#         stack.pop()

