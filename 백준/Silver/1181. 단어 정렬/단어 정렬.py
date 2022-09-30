T=int(input())
result=[]
for _ in range(1,T+1):
    result.append(input())
result=list(set(result))
# a=sorted(result,key=lambda x:x[0])
# a=sorted(a,key=lambda x:x[1])
# print(result)
result.sort()
# print(result)

b=sorted(result,key=lambda x:len(x))
for i in b:
    print(i)
