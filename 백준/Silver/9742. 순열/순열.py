def f(i,k):
    global cnt,str,result
    if i==k:
        cnt+=1

        if cnt==int(n):
            str=''.join(p)
            print(f'{arr} {n} = {str}')
            result+=1
            return 0


    else:
        for j in range(0,k):
            if used[j]==0:
                p[i]=arr[j]
                used[j]=1
                f(i+1,k)
                used[j]=0
while True:
    try:
        arr,n=input().split()
        used=[0]*len(arr)
        p=[0]*len(arr)
        cnt=0
        str=''
        result=0
        f(0,len(p))
        if result==0:
            print(f'{arr} {n} = No permutation')
    except:
        break


