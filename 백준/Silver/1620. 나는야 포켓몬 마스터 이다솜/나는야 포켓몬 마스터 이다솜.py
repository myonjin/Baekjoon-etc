import sys
from collections import deque
# from itertools import combinations
# from collections import deque
input=sys.stdin.readline

N,M= map(int,input().split())
arr1= {}
arr2= {}
for i in range(1,N+1):
    a=sys.stdin.readline().rstrip()
    arr1.setdefault(i,a)
    arr2.setdefault(a,i)
# print(arr1)
# print(arr2)
for _ in range(M):
    a=sys.stdin.readline().rstrip()
    if a.isdigit():
        print(arr1[int(a)])
    else:
        print(arr2[a])



# print(list(combinations(arr,3)))
# print(int(s/n))