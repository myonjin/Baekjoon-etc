import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
result = 999999999999999999999
i = 0
j = N-1

while i<j:
    sum = arr[i] + arr[j]
    if abs(result)>abs(sum):
        result=sum
    if sum < 0:
        i += 1
    else:
        j -= 1


print(result)