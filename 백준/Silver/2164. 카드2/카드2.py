import sys
from collections import deque
n=int(sys.stdin.readline())
li=deque([i for i in range(1,n+1)])
q2=li[0]
while len(li)>1:
    q1=li.popleft()
    q2=li.popleft()
    li.append(q2)
    # if len(li)==1:
    #     print(q2)
    #     break
print(q2)