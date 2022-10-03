N,S=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
for i in range(0,1 << N):
    s=0
    for j in range(0,N):
        if i & (1<<j):
            s+=arr[j]
    if s==S:
        cnt+=1
if S==0:
    cnt-=1
print(cnt)