import sys
# from collections import deque
n=int(sys.stdin.readline())
s=0
for i in range(1,n+1):
    s=0
    s+=i
    for j in str(i):
        s+=int(j)
    if s==n:
        print(i)
        break
else:
    print('0')
