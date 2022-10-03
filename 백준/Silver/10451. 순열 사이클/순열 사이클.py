import sys
sys.setrecursionlimit(10**6)
def find_set(x):
    global cnt,result
    if x==p[x]:
        cnt+=1
        return x

    else:
        if x not in ar:
            ar.append(x)
            result.append(x)
        else:
            cnt+=1
            return
        return find_set(p[x])


T= int(input())
for tc in range(T):
    N=int(input())
    p=[0]+ list(map(int,input().split()))
    # print(p)
    cnt=0
    result=[]
    ar=[]
    for i in range(1,N+1):
        if i not in result:
            find_set(i)
    print(cnt)