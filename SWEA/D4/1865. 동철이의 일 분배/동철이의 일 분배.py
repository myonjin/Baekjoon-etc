def f(i,k,per):
    global result

    if per==0:
        return
    # if arr[i][j]==0:
    #     return
    if per < result:
        return

    if i == k:
        # for di in range(N):
        #     cnt+=arr[di][ p[di] ]
        if result<=per:
            result=per


    else:
        for j in range(i,k):
            # if arr[i][p[i]]==0:
            #     continue
            p[i],p[j] = p[j], p[i]
            if arr[i][ p[i] ]:
                per*=arr[i][ p[i] ]/100
                f(i+1,k,per)
                per /= arr[i][p[i]]/100
                p[i],p[j] = p[j], p[i]
            else:
                p[i], p[j] = p[j], p[i]


T=int(input())
for tc in range(1,T+1):
    N=int(input()) #
    arr=[list(map(int,input().split())) for _ in range(N)]
    p=[i for i in range(N)]
    result=0
    # print(p)
    f(0,N,1)
    # print(arr)
    print(f'#{tc} {round(result*100,6):.6f}')