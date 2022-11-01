import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    stack=[]
    dic=dict()
    ans=1
    for _ in range(N):
        value,key=sys.stdin.readline().rstrip().split()
        if dic.get(key):
            dic[key]+=1
        else:
            dic[key]=1
            stack.append(key)
    for k in stack:
        ans=ans*(dic[k]+1)
    print(ans-1)


