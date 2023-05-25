def solution(s):
    print(s)
    anslen=100000
    for i in range(1,len(s)+1):
        ans=''
        count=0
        target=''
        for j in range(0,len(s),i):
            bu=s[j:j+i]
            if target != bu:
                if count >=2:
                    ans+=str(count) + target
                else:
                    ans+=target
                count=1
                target = bu
            else:
                target = bu
                count+=1
        else:
            if count >=2:
                ans+=str(count) + target
            else:
                ans+=target
        if anslen >= len(ans):
            anslen = len(ans)
    return anslen