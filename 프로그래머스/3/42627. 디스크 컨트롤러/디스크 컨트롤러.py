import heapq
def solution(jobs):
    answer = 0
    heap = []
    current_time = 0
    num = len(jobs)
    start = -1
    jobs.sort()
    k=0
    while k < num:
        temp = jobs[:]
        for job in temp:
            if job[0] <= current_time:
                heapq.heappush(heap,[job[1],job[0]])
                jobs.pop(0)
        if len(heap) > 0:
            current_job = heapq.heappop(heap)
            current_time += current_job[0]
            answer += current_time - current_job[1]
            k += 1
        else:
            current_time += 1
    return answer//num