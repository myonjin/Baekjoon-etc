import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())

M,N = map(int,input().split())
bam = [ 0 for _ in range(101)]
visited = [ 999 for _ in range(101)]
for _ in range(M+N):
    a,b = map(int,input().split())
    bam[a] = b

q = deque()
q.append(1)
visited[0]=0
visited[1]=0
while q:
    p = q.popleft()
    if p == 100:
        break
    for i in range(1,7):
        ip = p + i
        if 0<=ip<=100 and visited[ip]>visited[p]+1:
            if bam[ip] == 0:
                visited[ip] = visited[p] + 1
                q.append(ip)
            else:
                bp = bam[ip]
                if visited[bp] > visited[p] +1:
                    visited[bp] = visited[p] + 1
                    q.append(bp)
print(visited[100])