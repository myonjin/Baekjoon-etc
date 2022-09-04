T=int(input())
for tc in range(1,T+1):
    target=input()
    for i in range(1,11):
        pattern=target[:i] #맨처음 문자열과
        pattern2=target[i:i+i] #두번째 문자열이같으면
        if pattern==pattern2: 
            result=len(pattern) #그거출력
            break  # 제일짧은 문자열을 출력하기위해 중단
    print(f'#{tc} {result}')