import sys
from collections import deque
# from itertools import combinations
# from collections import deque
input=sys.stdin.readline

N,M= map(int,input().split())
arr=[]
for _ in range(N):
    n=int(input())
    arr.append(n)
arr.sort(reverse=True)
# print(arr)
cnt=0
for i in arr:
    if M//i:
        cnt+=M//i
        M=M%i
print(cnt)