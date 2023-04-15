from collections import deque
def solution(s):
    answer = True
    q=deque()
    for gal in s:
        if not q:
            q.append(gal)  
        else:
            if q[-1] == '(' and gal ==')':
                q.pop()
            else:
                q.append(gal)
    if q:
        return False
    else:
        return True 