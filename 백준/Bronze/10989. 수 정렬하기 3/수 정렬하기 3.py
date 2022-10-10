import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
N=[0]*10001
for i in range(T):
    n=int(sys.stdin.readline())
    N[n]+=1
for i in range(len(N)):
    for j in range(N[i]):
        print(i)
