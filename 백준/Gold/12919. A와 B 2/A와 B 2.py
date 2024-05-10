S = input()
T = input()
answer = 0

def dfs(T):
    global answer
    if T == S:
        answer = 1
        return
    if len(T) == 0:
        return

    if T[-1] == 'A':
        dfs(T[:-1])

    if T[0] == 'B':
        st = ''
        for c in T:
            st = c + st
        dfs(st[:-1])

dfs(T)

print(answer)