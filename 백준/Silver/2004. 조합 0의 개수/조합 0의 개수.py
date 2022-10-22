import sys
import math
input = sys.stdin.readline
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

# n = int(input())
N,M = map(int,sys.stdin.readline().split())

def f2(N):
    cnt_2=0
    while N != 0:
        N = N // 2
        cnt_2+=N
    return cnt_2

def f5(N):
    cnt_5=0
    while N != 0:
        N = N // 5
        cnt_5+=N
    return cnt_5
result_2=f2(N)-f2(M)-f2(N-M)
result_5=f5(N)-f5(M)-f5(N-M)

if result_2>0 and result_5>0:
    print(min(result_2,result_5))
else:
    print(0)




