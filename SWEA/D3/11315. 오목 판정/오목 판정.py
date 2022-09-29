T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result='NO'
    #가로줄 먼저 탐색
    for ar in arr:
        count=0
        for i in ar:
            if i=='o':
                count+=1
            else:
                count=0
            if count==5:
                result='YES'

    #세로줄 탐색
    arr_c=list(map(list,zip(*arr)))
    for ar in arr_c:
        count=0
        for i in ar:
            if i=='o':
                count+=1
            else:
                count=0
            if count==5:
                result='YES'


    #대각선 탐색
    for i in range(N):
        for j in range(N):              #전체 조사
            count = 0                   #오목판정 카운트
            if arr[i][j] == 'o':
                for c in range(1,5):    #오른쪽 위
                    if 0<=i-c<N and 0<=j+c<N and arr[i-c][j+c]=='o': # 인덱스 범위안이고( and는 앞부분 틀리면바로판별)
                        count +=1
                    else:
                        break
                    if count == 4:
                        result='YES'
                count = 0
                for c in range(1,5):    #오른쪽 아래
                    if 0<=i+c<N and 0<=j+c<N and arr[i+c][j+c]=='o': # 인덱스 범위안이고( and는 앞부분 틀리면바로판별)
                        count +=1
                    else:
                        break
                    if count == 4:
                        result='YES'
                count = 0
                for c in range(1,5):    #왼쪽 아래
                    if 0<=i+c<N and 0<=j-c<N and arr[i+c][j-c]=='o': # 인덱스 범위안이고( and는 앞부분 틀리면바로판별)
                        count +=1
                    else:
                        break
                    if count == 4:
                        result='YES'
                count = 0
                for c in range(1,5):    #왼쪽 위
                    if 0<=i+c<N and 0<=j-c<N and arr[i+c][j-c]=='o': # 인덱스 범위안이고( and는 앞부분 틀리면바로판별)
                        count +=1
                    else:
                        break
                    if count == 4:
                        result='YES'
                count = 0
    print(f'#{tc} {result}')

