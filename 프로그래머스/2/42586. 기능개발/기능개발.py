import math

def solution(progresses, speeds):
    answer = []
    day_arr = []
    
    # 각 작업의 완료까지 필요한 일수 계산
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        day_arr.append(day)
    
    # 첫 작업의 완료 일수로 최대 일수 초기화
    max_day = day_arr[0]
    cnt = 0
    
    # 각 작업의 완료 일수를 순회하면서 배포 일정 계산
    for day in day_arr:
        if day > max_day:
            # 현재 작업의 완료 일수가 이전 최대 완료 일수보다 크면 배포
            answer.append(cnt)
            max_day = day
            cnt = 1
        else:
            # 현재 작업을 이전 배포 일정에 포함시킴
            cnt += 1
    
    # 마지막 배포 일정 추가
    answer.append(cnt)
    
    return answer
