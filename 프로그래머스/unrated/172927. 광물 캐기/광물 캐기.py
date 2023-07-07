def solution(picks, minerals):
    answer = 0
    mineral_list = []
    tires = []
    for i in range(0,len(minerals),5):
        mineral_list.append(minerals[i:i+5])
    for mineral in mineral_list:
        tire = [0,0,0] # 다이아 철 돌
        for mine in mineral:
            if mine == 'diamond':
                tire[0] += 1
                tire[1] += 5
                tire[2] += 25
            elif mine == 'iron':
                tire[0] += 1
                tire[1] += 1
                tire[2] += 5
            elif mine == 'stone':
                tire[0] += 1
                tire[1] += 1
                tire[2] += 1
        tires.append(tire)
    if len(tires) > sum(picks):
        tires.pop()
    # print(tires)
    tires.sort(key = lambda x: -x[2])
    for tire in tires:
        if picks[0] > 0 :
            answer+=tire[0]
            picks[0]-=1
        elif picks[1] > 0 :
            answer+=tire[1]
            picks[1]-=1
        elif picks[2] > 0 :
            answer+=tire[2]
            picks[2]-=1
    
    
    return answer