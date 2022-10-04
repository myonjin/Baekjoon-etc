import sys
# from collections import deque
T= int(sys.stdin.readline())
arr=[[0]*14 for _ in range(15)]
for i in range(14):
    arr[0][i]=i+1
for i in range(14):
    arr[i][0]=1
for i in range(1,15):
    for j in range(14):
        arr[i][j]=arr[i][j-1]+arr[i-1][j]
# print(arr)
for _ in range (T):
    K=int(sys.stdin.readline())
    N=int(sys.stdin.readline())
    print(arr[K][N-1])