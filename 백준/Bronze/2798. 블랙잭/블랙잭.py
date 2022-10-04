import sys
from itertools import combinations
# from collections import deque
N,M= map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
# print(list(combinations(arr,3)))
m=0
for i in list(combinations(arr,3)):
    s=sum(i)
    if M>=s>m:
        m=s

print(m)
