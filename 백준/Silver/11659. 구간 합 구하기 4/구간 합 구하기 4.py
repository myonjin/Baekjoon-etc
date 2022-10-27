import sys
from collections import deque
# from itertools import combinations
# from collections import deque
N,M = map(int,sys.stdin.readline().split())
arr= list(map(int,sys.stdin.readline().split()))
arr_sum = [0]+arr
for i in range(1,N+1):
    arr_sum[i]+=arr_sum[i-1]
# print(arr_sum)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    print(arr_sum[b]-arr_sum[a-1])

