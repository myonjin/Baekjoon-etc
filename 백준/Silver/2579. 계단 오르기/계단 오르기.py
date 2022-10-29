import sys
import math
input = sys.stdin.readline
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# n = int(input())
N = int(sys.stdin.readline())
arr=[]
for _ in range(N):
    M = int(sys.stdin.readline())
    arr.append(M)
arr=[0]+arr
M=[0]*(N+1)
if N>0:
    M[1]=arr[1]
if N>1:
    M[2]=arr[1]+arr[2]
if N>=3:
    for i in range(3,N+1):
        a=arr[i]+arr[i-1]+M[i-3]
        b=arr[i]+M[i-2]
        M[i]=max(a,b)
print(M[N])



