def solution(answers):
    answer = []
    one = [1,2,3,4,5]             # 5
    two = [2,1,2,3,2,4,2,5]           # 8
    three = [3,3,1,1,2,2,4,4,5,5] # 10
    first,second,third=0,0,0
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            first+=1
        if answers[i] == two[i%8]:
            second+=1
        if answers[i] == three[i%10]:
            third+=1
    m_x=max(first,second,third)
    for ans in [(1,first),(2,second),(3,third)]:
        if ans[1] == m_x:
            answer.append(ans[0])
    return answer