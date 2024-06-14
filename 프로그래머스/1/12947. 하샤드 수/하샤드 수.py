def solution(x):
    answer = True
    temp = 0
    for t in str(x):
        temp += int(t)
        
    if x%temp == 0:
        pass
    else:
        answer = False
    return answer