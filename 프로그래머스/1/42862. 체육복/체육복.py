def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    for r in reserve[:]:
        if r-1 in lost:
            lost.remove(r-1)
            reserve.remove(r)
        elif r+1 in lost:
            lost.remove(r+1)
            reserve.remove(r)
    answer = n - len(lost)
    return answer