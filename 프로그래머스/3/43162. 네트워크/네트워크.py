def solution(n, computers):
    answer = 0
    node = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]==1:
                node[i].append(j)
    print(node)
            
    print(computers)
    
    
    
    return answer