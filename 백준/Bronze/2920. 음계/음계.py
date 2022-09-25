arr=list(map(int,input().split()))
result=0
for i in range(7):
    if arr[i]+1==arr[i+1]:
        result+=1
    elif arr[i]-1==arr[i+1]:
        result+=2
    else:
        print('mixed')
        break
if result==7:
    print('ascending')
elif result==14:
    print('descending')