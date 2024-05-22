def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if answer[-1] == a:
            pass
        else:
            answer.append(a)
    
        
    
    return answer