def solution(clothes):
    dic = {}
    for cloth in clothes:
        type = cloth[1]
        if type in dic:
            dic[type]+=1
        else:
            dic[type]=1
    sum = 1
    for val in dic.values():
        sum = sum * (val+1)
    answer = sum-1
    
    return answer