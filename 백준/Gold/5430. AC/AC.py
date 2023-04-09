import sys
from collections import deque

for _ in range(int(input())):
    P = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    li = sys.stdin.readline().strip()
    if li == '[]' and 'D' in P:
        print('error')
    elif li == '[]' and 'R' in P:
        print('[]')
    else:
        count=0
        li = li.strip("[]")
        q =deque()
        li_2 = li.split(',')
        for a in li_2:
            q.append(int(a))
        for p in P:
            if p == 'R':
                count+=1
            elif p == 'D':
                if count % 2 == 0:
                    if len(q)==0:
                        print('error')
                        break
                    else:
                        q.popleft()
                else:
                    if len(q)==0:
                        print('error')
                        break
                    else:
                        q.pop()
        else:
            if count%2==0:
                print('['+",".join(str(x) for x in list(q))+']')
            else:
                q.reverse()
                print('['+",".join(str(x) for x in list(q))+']')
