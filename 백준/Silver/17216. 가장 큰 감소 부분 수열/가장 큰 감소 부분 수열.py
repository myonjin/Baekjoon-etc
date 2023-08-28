N = int(input())
arr = list(map(int,input().split()))
dp = [0]*N
# dp[N-1] = arr[N-1]
for i in range(N-1,-1,-1):
    dp[i] = arr[i]
    for j in range(i,N):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],arr[i] + dp[j])
print(max(dp))