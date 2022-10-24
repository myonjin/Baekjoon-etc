import sys
from collections import deque
# from itertools import combinations
# from collections import deque
input=sys.stdin.readline

# N,M= map(int,input().split())
a= sys.stdin.readline().rstrip().split('-')
# print(a)
n=0

for j in range(len(a)):
    s=a[j].split('+')
    if j ==0:
        for i in s:
            n+=int(i)
    else:
        for i in s:
            n-=int(i)
print(n)
# print(list(combinations(arr,3)))
# print(int(s/n))