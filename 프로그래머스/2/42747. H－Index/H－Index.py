def solution(citations):
    answer = 0
    h = 0
    N = len(citations)
    citations.sort(reverse = True)
    for idx,c in enumerate(citations):
        if idx >= c:
            return idx
    
    return N