import sys
N,M= map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
m=max(arr)

start=1
end=m

while start<=end:
    result=0
    mid = (start+end)//2
    for i in arr:
        if i>mid:
            result+=i-mid
    if result>=M:
        start=mid+1
    else:
        end=mid-1
print(end)
