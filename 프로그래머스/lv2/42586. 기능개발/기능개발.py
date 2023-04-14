import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    stack = []
    q= deque()
    for i in range(len(progresses)):
        stack.append(math.ceil((100-progresses[i])/speeds[i]))
    print(stack)
    high=0
    for s in stack:
        if not q:
            q.append(s)
        else:
            if q[0] >= s:
                q.append(s)
            else:
                answer.append(len(q))
                q=deque()
                q.append(s)
    answer.append(len(q))
    return answer