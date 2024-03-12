def solution(park, routes):
    answer = [0,0]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                r=i
                c=j       
    for route in routes:
        d,n = route.split(" ")
        n = int(n)
        print(r,c)
        if d == "N":
            if 0<=r-n<len(park):
                pass
            else:
                continue
            dr = r
            for _ in range(n):
                if park[dr-1][c] !='X' : 
                    dr-=1
                else:
                    break
            else:
                r = dr
        elif d == "S":
            if 0<=r+n<len(park):
                pass
            else:
                continue
            dr = r
            for _ in range(n):
                if park[dr+1][c] !='X' : 
                    dr+=1
                else:
                    break
            else: 
                r = dr
        elif d == "W":
            if 0<=c-n<len(park[0]):
                pass
            else:
                continue
            dc = c
            for _ in range(n):
                if park[r][dc-1] !='X' : 
                    dc-=1
                else:
                    break
            else:
                c = dc
        elif d == "E":
            if 0<=c+n<len(park[0]):
                pass
            else:
                continue
            dc = c
            for _ in range(n):
                if park[r][dc+1] !='X' : 
                    dc+=1
                else:
                    break
            else:
                c = dc
    answer[0] = r
    answer[1] = c
             
    return answer