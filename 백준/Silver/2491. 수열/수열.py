import sys
# from collections import Counter
# from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# N,M,B = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
T=int(input())
arr= list(map(int,sys.stdin.readline().split()))
cnt=0
result=0
for i in range(T):
    if i==0:
        cnt+=1
    else:
        if arr[i-1]<=arr[i]:
            cnt+=1
        else:
            cnt=1
        num=arr[i]
    if cnt>result:
        result=cnt
arr.reverse()
cnt=0
for i in range(T):
    if i==0:
        cnt+=1
    else:
        if arr[i-1]<=arr[i]:
            cnt+=1
        else:
            cnt=1
        num=arr[i]
    if cnt>result:
        result=cnt
print(result)









