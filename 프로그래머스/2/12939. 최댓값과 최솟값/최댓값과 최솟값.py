def solution(s):
    
    arr = list(map(int,s.split(" ")))
    ans = [str(min(arr)),str(max(arr))]
    # print(ans)
    answer= " ".join(ans)
    print(answer)
    return answer