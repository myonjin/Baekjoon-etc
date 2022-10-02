K, N = map(int,input().split())
lansun= [int(input()) for _ in range(K)]
# arr= [i for i in range(1,max(lansun)+1)]
# print(arr)
start,last=1,max(lansun)
max_len=0

while start<=last:
    mid= (start + last)//2
    sum=0
    for ar in lansun:
        # print(mid,type(mid))
        sum+=ar//mid
    # print(sum,start,last)
    # if sum==N and mid>=max_len:
    #     max_len=mid
    #     start=mid+1
    # print(start)
    # print(sum)
    if sum < N:
        last = mid - 1
    else:
        start = mid + 1
    # print(mid)
    # print(last)
    # print('------')
# print(start)
# print(mid)
print(last)

