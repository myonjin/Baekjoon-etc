N=int(input())
arr=list(map(int,input().split()))
result=0
for ar in arr:
    cnt=0
    for i in range(1,ar+1):
        if ar==1:
            break
        if ar%i==0:
            cnt+=1
        if cnt>2:
            break
    if cnt==2:
        result+=1
print(result)
