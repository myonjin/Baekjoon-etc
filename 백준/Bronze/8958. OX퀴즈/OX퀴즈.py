N=int(input())
for _ in range(N):
    arr=input()
    result=''
    score=0
    for ar in arr:
        if ar=='O':
            result+=ar
            score+=len(result)
        elif ar=='X':
            result=''
    print(score)