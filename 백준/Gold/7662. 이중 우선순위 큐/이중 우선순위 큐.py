
import sys
from collections import deque
import heapq
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
# arr=[[] for _ in range(N+1)]
# visited=[0]*(N+1)
# q=deque()

# arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

T=int(sys.stdin.readline())
for _ in range(T):
    N= int(sys.stdin.readline())
    heap_min=[]
    heap_max=[]
    visited=[0]*(N+1)
    for i in range(N):
        q,num=sys.stdin.readline().split()
        num=int(num)
        if q=='I':
            heapq.heappush(heap_min,(num,i))
            heapq.heappush(heap_max,(-num,i))
            visited[i]=1
        else:
            if num==1: # 최대값
                while heap_max and not visited[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                if heap_max:
                    visited[heapq.heappop(heap_max)[1]]=0
            else:      # 최소값
                while heap_min and not visited[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                if heap_min:
                    visited[heapq.heappop(heap_min)[1]]=0
    while heap_max and not visited[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not visited[heap_min[0][1]]:
        heapq.heappop(heap_min)
    if heap_min:
        print(-heapq.heappop(heap_max)[0],heapq.heappop(heap_min)[0])

    else:
        print('EMPTY')