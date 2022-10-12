import sys
# from collections import Counter
# from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
T=int(input())
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split()) #  가로 세로
    arr=[[0]*M for _ in range(N)]
    stack=list()
    for _ in range(K):
        a,b=map(int,sys.stdin.readline().split())
        arr[b][a]=1
        stack.append([b,a])
    cnt=0
    for i,j in stack:
        if arr[i][j]==1:
            s=[]
            s.append([i,j])
            arr[i][j]=0
            while s:
                i,j=s.pop()
                for d_i,d_j in [[1,0],[-1,0],[0,-1],[0,1]]:
                    di, dj = i + d_i, j+d_j
                    if 0 <= di < N and 0 <= dj < M and arr[di][dj] == 1:
                        arr[di][dj] = 0
                        s.append([di, dj])
            cnt+=1

    # print(*arr,sep='\n')
    print(cnt)








