import sys
input = sys.stdin.readline
from collections import deque

N, M, A, B = map(int, input().split())
dp = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        visited[i] = True

dp[N] = 0
q = deque()
q.append(N)
while q:
    val = q.popleft()
    if val == 0:
        break
    for i in (val-A, val-B):
        if i >= 0:
            if visited[i]:
                continue
            else:
                q.append(i)
                dp[i] = dp[val] + 1
                visited[i] = True
if dp[0]:
    print(dp[0])
else:
    print(-1)