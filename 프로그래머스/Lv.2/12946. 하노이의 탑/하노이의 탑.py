def solution(n):
    global answer
    answer = []
    hanoi(n,1,2,3)
    return answer


def hanoi(n,s,m,t):
    if n == 1:
        answer.append([s,t])
    else:
        hanoi(n-1,s,t,m)
        hanoi(1,s,m,t)
        hanoi(n-1,m,s,t)
    return 0
    