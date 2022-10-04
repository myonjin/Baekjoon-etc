import sys
# from itertools import combinations
# from collections import deque
N= int(sys.stdin.readline())
arr=[]
for _ in range(N):
    a,b=sys.stdin.readline().split()
    a=int(a)
    arr.append([a,b])
arr.sort(key=lambda x:x[0])
for ar in arr:
    print(*ar)
# N,M= map(int,sys.stdin.readline().split())
# arr=list(map(int,sys.stdin.readline().split()))
# print(list(combinations(arr,3)))

