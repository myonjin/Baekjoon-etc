import sys
T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    result=''
    if N%H==0:
        h=str(H)
    else:
        h=str(N%H)
    if N%H==0:
        ho=str(N//H)
    else:
        ho=str(N//H+1)
    result=h+ho.zfill(2)
    print(result)


