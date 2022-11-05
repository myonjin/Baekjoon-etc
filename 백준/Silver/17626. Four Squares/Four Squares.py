import sys
import heapq
# from collections import Counter
# from collections import deque
# arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# n = int(input())
N = int(sys.stdin.readline())
arr = [5]*(N+1)
arr[0]=0

for j in range(1,N+1):
        # for i in range(1,224):
        #     if i**2<=j<(i+1)**2:
        #         if j-i**2==0:
        #             arr[j]=1
        #             break
    for k in range(1,224):
        if j<k**2:
            break
        arr[j]=min(arr[j],arr[j-k**2]+1)

print(arr[N])
# print(arr)



