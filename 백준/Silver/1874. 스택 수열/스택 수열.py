import sys
n=int(input())
arr=[]
li=[i for i in range(1,n+1)]
result=[]
ans=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
c=0
# print(arr)
for i in li:
    result.append(i)
    ans.append('+')

    while True:
        # print(result)
        if result and arr and result[-1]==arr[0]:
            arr.pop(0)
            result.pop()
            ans.append('-')
        elif result and arr and i==n and result[-1]!=arr[0]:
            print('NO')
            c+=1
            break
        else:
            break
if c==0:
    for i in ans:
        print(i)
