def solution(priorities, location):
    answer = 0
    arr = []
    for i in range(len(priorities)):
        arr.append([i,priorities[i]])
    print(arr)
    count = 0
    while len(priorities)>0:
        idx, value = arr.pop(0)
        if value == max(priorities):
            count+=1
            if idx == location:
                answer = count 
                break
            priorities.remove(value)
        else:
            arr.append([idx,value])
        
        
    return answer