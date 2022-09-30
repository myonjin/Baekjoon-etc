s=input()
a=[]
for i in range(97,123):
    a.append(chr(i))
m=0
for i in a:
    m = 0
    for j in s:
        # print(i,j)
        if i==j:
            print(m,end=' ')
            break
        m+=1

    else:
        print(-1,end=' ')