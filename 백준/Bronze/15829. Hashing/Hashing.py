import sys
from collections import deque
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))
T=int(input())
chr=input()
sum=0
for i in range(T):
    sum+=(ord(chr[i])-96)*(31**i)
print(sum)

