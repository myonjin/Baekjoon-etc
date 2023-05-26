def solution(n, lost, reserve):
    answer = 0
    newlost = list(set(lost) - set(reserve))
    newreserve = list(set(reserve) - set(lost))
    lost.sort
    reserve.sort
    for i in newreserve:
        for j in newlost:
            if j == i-1:
                newlost.remove(j)
                break
            elif j == i+1:
                newlost.remove(j)
                break
            
    answer = n - len(newlost)
    return answer