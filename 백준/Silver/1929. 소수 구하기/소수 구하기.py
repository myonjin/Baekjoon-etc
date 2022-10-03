import sys
N,M=map(int,(sys.stdin.readline().split()))
li=[1]*(M+1)
li[0]=0
li[1]=0
for i in range(2,int(M**0.5+1)):
    if li[i]:
        for j in range(i*2,M+1,i):
            li[j]=0
for i in range(N,M+1):
    if li[i]==1:
        print(i)
