N = int(input())
T = [0]*(N+2)
P = [0]*(N+2)
dp = [0]*(N+2)
for i in range(1,N+1):
    a,b = map(int,input().split())
    T[i] = a
    P[i] = b
# print(T,P)

for i in range(N,-1,-1):
    if i + T[i] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])
# print(P)
print(max(dp))
# print(dp)