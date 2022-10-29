import sys
import heapq
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# n = int(input())
N = int(sys.stdin.readline())
hq=[]
for _ in range(N):
    M=int(sys.stdin.readline())
    if M==0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq,M)

