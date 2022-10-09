import sys
# from itertools import combinations
# from collections import deque
# N= int(sys.stdin.readline())
N,M= map(int,sys.stdin.readline().split())
s=1
n=1
for i in range(M):
    s=s*(N-i)
    n=n*(M-i)
# arr=list(map(int,sys.stdin.readline().split()))
# print(list(combinations(arr,3)))
print(int(s/n))