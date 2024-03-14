def solution(number, limit, power):
    arr=[]
    answer = 0
    def devisor(num):
        count = 0
        for i in range(1,int(num**(1/2))+1):
            if num%i == 0:
                count+=1
                if num//i != i:
                    count+=1
        return count
    for i in range(1,number+1):
        arr.append(devisor(i))
    for ar in arr:
        if limit<ar:
            answer+=power
        else:
            answer+=ar
    return answer