import heapq
def solution(scoville, K):
    hq=[]
    answer = 0
    for sco in scoville:
        heapq.heappush(hq,sco)
    while True:
        if hq[0] >= K:
            break
        if len(hq)<2:
            return -1
        first = heapq.heappop(hq)
        second = heapq.heappop(hq)
        mix = first + second * 2
        heapq.heappush(hq,mix)
        answer+=1
    return answer