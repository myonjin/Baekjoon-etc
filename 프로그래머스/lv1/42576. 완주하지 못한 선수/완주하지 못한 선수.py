def solution(participant, completion):
    answer = ''
    dic={}
    for com in participant:
        dic[com] = dic.get(com, 0) + 1
    for com in completion:
        dic[com]-=1
    for key,value in dic.items():
        if value ==1:
            answer=key
            break
    return answer