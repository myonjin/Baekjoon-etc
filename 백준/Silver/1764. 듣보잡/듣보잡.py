import sys

N,M=map(int,sys.stdin.readline().split())
listen=dict()
see=dict()
for i in range(N):
    a=sys.stdin.readline().rstrip()
    listen[a]=i
for _ in range(1,M):
    b=sys.stdin.readline().rstrip()
    see[b]=1
# print(listen)
# print(see)
m=min(N,M)
# for i in range()
s=[]

for i in listen:
    if see.get(i)==1:
        s.append(i)
s.sort()
print(len(s))
print(*s, sep='\n')
