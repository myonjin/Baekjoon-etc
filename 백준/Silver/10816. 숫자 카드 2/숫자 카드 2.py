import sys
from collections import Counter
# A,B,C = map(int,sys.stdin.readline().split())
# arr= list(map(int,sys.stdin.readline().split()))

n=int(sys.stdin.readline())
target= sys.stdin.readline().split()
m=int(sys.stdin.readline())
pattern = list(map(int,sys.stdin.readline().split()))
# print(Counter(target))
a=Counter(target)
# print(a)
for i in pattern:
    if a.get(str(i)):
        print(a.get(str(i)),end=' ')
    else:
        print(0,end=' ')




