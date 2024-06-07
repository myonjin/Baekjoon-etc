answer = 50
def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    dfs(begin,target,words,visited,0)
    return answer


def dfs(begin,target,words,visited,step):
    global answer
    if answer <= step:
        return 0
    if begin==target:
        answer = min(answer,step)
    for i in range(len(words)):
        if wordtest(begin,words[i]) and visited[i] == False:
            visited[i] = True
            dfs(words[i],target,words,visited,step+1)
            visited[i] = False



# True : 다르다
def wordtest(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            count +=1
    if count == 1:
        return True
    else:
        return False
    



