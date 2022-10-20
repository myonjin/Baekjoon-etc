import sys
# from itertools import combinations
# from collections import deque
# N,M= map(int,sys.stdin.readline().split())
N= int(sys.stdin.readline())
M= int(sys.stdin.readline())
if M==0:
    if abs(100-N)>len(str(N)):
        print(len(str(N)))
    else:
        print(abs(100-N))

else:
    arr=list(map(str,sys.stdin.readline().split()))
    min_result=abs(N-100)
    for i in range(0,1000000):
        cnt=0
        result=0
        for j in str(i):
            if j in arr:
                cnt+=1
                break
        # 0에서 터치하는식으로
        if cnt!=0:
            continue
        result = abs(N - i) + len(str(i))

        if result<min_result:
            min_result=result
    print(min_result)



# print(list(combinations(arr,3)))
# print(int(s/n))