n,m=map(int,input().split())
answer=1

for i in range(1,m+1):
    answer=answer*(n-i+1)//i
print(answer)