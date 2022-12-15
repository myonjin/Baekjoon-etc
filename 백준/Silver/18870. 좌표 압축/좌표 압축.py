
import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
# arr=[[] for _ in range(N+1)]
# visited=[0]*(N+1)
# q=deque()

N= int(sys.stdin.readline())
arr_1=list(map(int,sys.stdin.readline().split()))
# arr.sort()
# print(arr)
arr= list(set(arr_1))
arr.sort()
# arr_set.sort()
# print(arr_set)
dic={}
for i in range(len(arr)):
    if arr[i] in dic:
        continue
    else:
        dic[arr[i]]=i
# print(dic)
answer=[0]*N
for i in arr_1:
    print(dic[i],end=' ')


