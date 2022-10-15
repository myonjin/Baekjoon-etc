import sys
# from collections import Counter
# from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
N,r,c = map(int,sys.stdin.readline().split())
cnt=0
while N!=0:
    N-=1
    visit=(2**N)*(2**N)
    if r<2**N and c<2**N:
        cnt+=0


    elif c>=2**N and r<2**N:
        cnt+=visit
        c = c - 2 ** N
    elif c<2**N and r>=2**N:
        cnt+=visit*2
        r = r - 2 ** N
    elif r>=2**N and c>=2**N:
        cnt+=visit*3
        r = r - 2 ** N
        c = c - 2 ** N

print(cnt)







