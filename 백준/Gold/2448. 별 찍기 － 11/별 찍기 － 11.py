import sys
import math
input = sys.stdin.readline
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# N,r,c = map(int,sys.stdin.readline().split())

n = int(input())

stars = [[' ']*2*n for _ in range(n)]

def f(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    else:
        newsize=size//2
        f(i,j,newsize)
        f(i+newsize,j-newsize,newsize)
        f(i+newsize,j+newsize,newsize)

f(0,n-1,n)
for star in stars:
    print(''.join(star))







