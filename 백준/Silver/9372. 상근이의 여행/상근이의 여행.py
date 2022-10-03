import sys
T=int(input())
for tc in range(T):
    arr=[]
    N,M=map(int,input().split())
    for _ in range(M):
        a,b=map(int,sys.stdin.readline().split())
        arr.append([a,b])
    print(N-1)
