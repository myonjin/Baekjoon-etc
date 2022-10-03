N=int(input())
arr=[]

for _ in range(N):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort()
arr.sort(key=lambda x:x[1])
# print(arr)
# for ar in arr:
#     if not result:
#         result.append(ar)
#     if result[-1][1]<=ar[0]:
#         result.append(ar)
s=0
e=0
cnt=0
for ar in arr:
    if e<=ar[0]:
        cnt+=1
        e=ar[1]


print(cnt)