import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
target=list(map(int,sys.stdin.readline().split()))
arr.sort()
# print(arr)
start=arr[0]
end=arr[-1]
for i in target:
    start = 0
    end = N-1
    if i > arr[-1]:
        print(0)
        continue
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==i:
            print('1')
            break
        elif arr[mid]>i:
            end=mid-1
        else:
            start=mid+1
    if start>end:
        print(0)
