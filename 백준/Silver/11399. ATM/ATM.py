import sys
from collections import deque
# from itertools import combinations
# from collections import deque
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
arr.sort()
s=0
for i in range(N):
    s+=arr[i]*(N-i)
print(s)