from collections import deque
import sys
T= int(input())
for _ in range(T):
    N,M=map(int,(sys.stdin.readline().split()))
    q=deque(list(map(int,(sys.stdin.readline()).split())))
    index=deque([i for i in range(N)])
    # print(index)
    cnt=1
    while q:
        if q[0]==max(q) and index[0]==M:
            break
        elif q[0]==max(q):
            q.popleft()
            index.popleft()
            cnt+=1
        else:
            s=q.popleft()
            q.append(s)
            s=index.popleft()
            index.append(s)
    print(cnt)


