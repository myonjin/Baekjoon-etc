def solution(numbers, target):
    answer = 0
    def dfs(cnt,result):
        nonlocal answer
        if cnt == len(numbers):
            if  result == target:
                answer+=1
            return
        else:
            dfs(cnt+1,result+numbers[cnt])
            dfs(cnt+1,result-numbers[cnt])
            
    dfs(0,0)
    
    
    return answer