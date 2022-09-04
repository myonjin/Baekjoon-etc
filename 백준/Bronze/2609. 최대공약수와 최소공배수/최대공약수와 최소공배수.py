N,M=map(int,input().split())
divisor = 1 #약수
multiple = 1 #배수
i=2
while i<=M:
    if N % i == 0 and M % i == 0:
        N = N // i
        M = M // i
        divisor = divisor * i
        continue
    else:
        i+=1
multiple=N*M*divisor
print(divisor)
print(multiple)