T=int(input())
for _ in range(T):
    a,b=input().split()
    a=int(a)
    result=''
    for tem in b:
        result+=tem*a
    print(result)