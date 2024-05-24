def solution(array, commands):
    answer = []
    arr = []
    for command in commands:
        s = command[0]-1
        e = command[1]
        n = command[2]-1
        arr = array[s:e]
        arr.sort()
        answer.append(arr[n])       
    return answer