import sys
N=int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for _ in range(N)]
s_arr=sum(arr)
# print(s_arr)
# print(s_arr/N)
# print(round(s_arr/N))
if s_arr<0:
    print(round(s_arr/N))
else:
    print(round(s_arr/N))
arr.sort()

print(arr[N//2])
# if N%2==1:
# else:
#     print(arr[N//2]+arr[N//2-1])
ind=[0]*8001
li=[]
# print('000')
for ar in arr:
    if ar>=0:
        ind[ar]+=1
    else:
        ind[-ar+4000]+=1
# print(ind)
max_index=max(ind)
for i in range(len(ind)):
    if max_index==ind[i]:
        if i >= 4001:
            li.append(-(i-4000))
        else:
            li.append(i)
# print(li)
li.sort()
if len(li)>1:
    print(li[1])
else:
    print(li[0])
# print('000')

print(max(arr)-min(arr))