A=int(input())
B=int(input())
C=int(input())
result=list(str(A*B*C))
D=list(map(int,result))

for i in range(0,10):
    print(D.count(i))
