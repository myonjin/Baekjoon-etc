N = int(input())
visited = [0] * (N+1)
answer = 0
def queen(k):
    global answer
    if k == N:
        answer += 1
    else:
        for i in range(N):
            visited[k] = i
            if promising(k):
                queen(k+1)
            visited[k] = 0

def promising(k):
    j = 0
    while j < k:
        if visited[j] == visited[k] or abs(k - j) == abs(visited[k] - visited[j]):
            return False
        j += 1
    return True

queen(0)

print(answer)