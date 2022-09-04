T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input()))
    clap=0
    result=0
    #변수설정
    for i in range(len(arr)):
        count=0
        if clap<i:
            count+=i-clap
            clap+=count
            result+=count
        clap+=arr[i]
    print(f'#{tc} {result}')