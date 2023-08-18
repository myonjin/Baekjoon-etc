# T = int(input())
# N = int(input())
# arr = list(map(int,input().split()))
# for _ in range(T):
N,d,k,c = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(int(input()))
max_len = 0
for i in range(N):
    ar= set()
    for j in range(k):
        ij = i+j
        if ij>=N:ij-=N
        ar.add(arr[ij])
    if len(ar)>=max_len:
        if c not in ar:
            max_len= len(ar) +1
        else:
            max_len=len(ar)
print(max_len)