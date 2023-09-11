from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + arr[i-1][j-1]
ans = 0
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    ans = cum[x2][y2] - cum[x2][y1-1] - cum[x1-1][y2] + cum[x1-1][y1-1]
    print(ans)
