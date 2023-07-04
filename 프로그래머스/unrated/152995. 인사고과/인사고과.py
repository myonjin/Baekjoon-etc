def solution(scores):
    answer = 1
    wonho = scores[0]
    wonho_sum = sum(wonho)
    scores.sort(key= lambda x : (-x[0],x[1]) )
    review = 0

    for score in scores:
        if wonho[0] < score[0] and wonho[1]< score[1]:
            return -1
        if review <= score[1]:
            review = score[1]
            if wonho_sum <score[0]+score[1]:
                answer+=1
    return answer