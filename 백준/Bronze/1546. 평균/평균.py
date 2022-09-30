N=int(input())
arr=list(map(int,input().split()))
m=max(arr)
b=0
result=[]
for i in arr:
    b=i/max(arr)*100
    result.append(b)
# print(result)
su=0
cnt=0
for i in result:
    su+=i
    cnt+=1
print(su/cnt)