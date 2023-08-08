import sys
input = sys.stdin.readline

N = int(input())
arr =[0] + list(map(int,input().split()))
dp = [0]*(N+1)
dp[1] = arr[1]
dp[2] = max(arr[1]*2,arr[2])
# dp [i] = dp[i-1] + dp[1] or dp[i-2] + dp[2] or arr[i]
# dp [2] = dp[1] + arr[1] or arr[2]
# dp [3] = dp[1] + dp[2] or arr[3] or arr[
for i in range(1,N+1):
    if (i==1 or i==2):
        continue
    for j in range(1,i+1):
        dp[i] = max(dp[i],arr[j]+dp[i-j])
print(dp[N])