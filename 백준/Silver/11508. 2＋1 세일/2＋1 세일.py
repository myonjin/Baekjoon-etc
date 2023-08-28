N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
cnt = 0
for i in range(N):
    if (i+1)%3 == 0:
        continue
    cnt+=arr[i]
print(cnt)