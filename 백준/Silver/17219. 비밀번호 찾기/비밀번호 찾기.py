import sys
from collections import deque
# from itertools import combinations
# from collections import deque
N,M = map(int,sys.stdin.readline().split())
dic=dict()
for _ in range(N):
    a,b=sys.stdin.readline().rstrip().split()
    dic[a]=b
# print(dic)
for _ in range(M):
    n=sys.stdin.readline().rstrip()
    # print(n)
    print(dic[n])
