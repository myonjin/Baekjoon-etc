import sys
# from collections import Counter
# from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
# N,M,B = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
T=int(input())
arr=[[0,0] for _ in range(41)]
arr[0][0],arr[0][1]=1,0
arr[1][0],arr[1][1]=0,1
for i in range(2,41):
    arr[i][0]=arr[i-1][0]+arr[i-2][0]
    arr[i][1]=arr[i-1][1]+arr[i-2][1]
for _ in range(T):
    n=int(input())
    print(*arr[n])











