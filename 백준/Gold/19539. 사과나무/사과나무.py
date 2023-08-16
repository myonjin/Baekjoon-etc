N = int(input())
arr = list(map(int,input().split()))
sum_2= 0
for ar in arr:
    sum_2 += ar//2

if (sum(arr)//3 <= sum_2) and sum(arr)%3==0:
    print("YES")
else:
    print("NO")
