def solution(triangle):
    answer = 0
    dp = []
    for i in range(1,len(triangle)+1):
        dp.append([0]*i)
    dp[0][0] = triangle[0][0]
    # for d in dp:
    #     print(d)
    # for t in triangle:
    #     print(t)
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i-1][j-1] +triangle[i][j] , triangle[i-1][j] + triangle[i][j])
            
    # for d in dp:
    #     print(d)
    # for t in triangle:
    #     print(t)            
            
        
    return max(triangle[-1])