import heapq
def solution(scoville, K):
    hq = []
    for s in scoville:
        heapq.heappush(hq,s)
    count = 0
    while hq[0] < K:
        if len(hq) <= 1:  # 힙에 남은게 2개미만 일때
            return -1
        count +=1
        f = heapq.heappop(hq)
        s = heapq.heappop(hq)
        mix = f + s * 2
        heapq.heappush(hq,mix)
    if count and hq[0] < K == 0:
        return -1
    else:
        return count

    # 테스트 18번 반례 
    # 