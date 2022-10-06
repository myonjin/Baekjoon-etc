import sys
# from itertools import combinations
# from collections import deque
N= int(sys.stdin.readline())
# N,M= map(int,sys.stdin.readline().split())
result=0
while N>=0:
    if N%5==0:
        result+=N//5
        print(result)
        break
    else:
        N-=3
        result+=1
else:
    print(-1)



# arr=list(map(int,sys.stdin.readline().split()))
# print(list(combinations(arr,3)))
# print(int(s/n))