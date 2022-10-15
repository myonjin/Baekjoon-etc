import sys
import math
# from collections import Counter
# from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# N,r,c = map(int,sys.stdin.readline().split())
N=int(input())
F=str(math.factorial(N))
cnt=0
# print(F)
for i in range(len(F)-1,-1,-1):
    if F[i]=='0':
        cnt+=1
    else:
        break
print(cnt)






