# A 만큼 피로도 쌓이고 B만큼 일처리
# 한시간 쉬면 피로도 C 만큼 줄어듬  M 넘기면안됨
# 5 3 2 10
# 한시간 일  5만큼 쌓이고 3만큼 처리 한시간쉬면 2 차감 10넘기면안됨
# 1 / 5 3
# 2 / 10 6
# 3 / 8 6
# 4 / 6 6
# 5 / 4 6
# 6 / 9 9

A,B,C,M = map(int,input().split())
hour = 0
work = 0
hard = 0
while hour<24:
    hour+=1
    if hard+A<=M:
        work+=B
        hard+=A
    else:
        hard-=C
        if hard<0:
            hard=0
print(work)