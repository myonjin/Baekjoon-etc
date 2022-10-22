import sys
import math
input = sys.stdin.readline
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# N,r,c = map(int,sys.stdin.readline().split())
N=int(input())
arr=[0]*1000001
arr[2]=1
arr[3]=1
arr[4]=2
arr[5]=3
arr[6]=2
arr[7]=3
for i in range(8,N+1):
    if i%6==0:
        arr[i]=min(arr[i//2]+1,arr[i-1]+1,arr[i//3]+1)
    elif i%2==0:
        arr[i]=min(arr[i//2]+1,arr[i-1]+1)
    elif i%3==0:
        arr[i]=min(arr[i//3]+1,arr[i-1]+1)
    else:
        arr[i]=arr[i-1]+1
print(arr[N])






