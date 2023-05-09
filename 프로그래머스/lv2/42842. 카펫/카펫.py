def solution(brown, yellow):
    answer = []
    yellow_sum = (brown - 4)//2
    for i in range(1,yellow_sum//2+1):
        if (i*(yellow_sum-i)==yellow):
            yellow_list=[i,yellow_sum-i]
    answer=[2+max(yellow_list),2+min(yellow_list)]
    return answer