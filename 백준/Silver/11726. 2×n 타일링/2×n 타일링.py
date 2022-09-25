N = int(input())
arr=[0]*1001
arr[1]=1
arr[2]=2
i=3
while i<=N:
    arr[i]=arr[i-1]+arr[i-2]
    i+=1
print(arr[N]%10007)