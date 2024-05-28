def solution(name):
    answer = 0
    cnt = 9999999999
    for n in name:
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
    
    # 하나하나 문자열을 시작하는 A연속 문자열 찾기
    for i,n in enumerate(name):
        # 현재 문자열의 다음부터 찾기
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx+=1
        
        # i 는 시작 문자열 idx는 A문자열의 끝 점 
        # BAAAABBABB 일때 처음 i는 0 idx는 5 ,  0 + (len(name) - 5) + min(왼,오)
        cnt = min(cnt,i+(len(name)-idx)+min(i,len(name)-idx))
    
    answer = answer + cnt
    return answer