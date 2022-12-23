import sys
from collections import deque
# from itertools import combinations
# from collections import deque
# N,M = map(int,sys.stdin.readline().split())
# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())
# arr=[[] for _ in range(N+1)]
# visited=[0]*(N+1)
# q=deque()
def paper(s_i,s_j,size):
    global result
    pan=0
    if arr[s_i][s_j]==0:
        for i in range(s_i,s_i+size):
            for j in range(s_j,s_j+size):
                if arr[i][j]!=0:
                    pan=1
                    break
            if pan:
                break
    if arr[s_i][s_j]==1:
        for i in range(s_i,s_i+size):
            for j in range(s_j,s_j+size):
                if arr[i][j]!=1:
                    pan=1
                    break
            if pan:
                break

    if pan==0:
        result='('+str(arr[s_i][s_j])+')'
        return arr[s_i][s_j]
    else:
        size=size//2
        paper(s_i,s_j,size)
        paper(s_i,s_j+size,size)
        paper(s_i+size,s_j,size)
        paper(s_i+size,s_j+size,size)
        return '('+str(paper(s_i,s_j,size))+str(paper(s_i,s_j+size,size))+str(paper(s_i+size,s_j,size))+str(paper(s_i+size,s_j+size,size))+')'

N= int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
# print(arr)
result=''
# paper(0,0,N)
print(paper(0,0,N))
# print(arr)
# print(visited)