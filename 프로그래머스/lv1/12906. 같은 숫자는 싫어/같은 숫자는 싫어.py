from collections import deque
def solution(arr):
    answer = deque()
    for num in arr:
        if not answer:
            answer.append(num)
        else:
            if answer[-1] != num:
                answer.append(num)
    return list(answer)