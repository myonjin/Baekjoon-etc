import sys
# from collections import deque
n=int(sys.stdin.readline())
i=0
j=2
cnt=1
while n>1:
   if j<=n<j+6*i:
       print(cnt)
       break
   else:
       j=j+6*i
       cnt+=1
       i+=1
if n==1:
    print(1)