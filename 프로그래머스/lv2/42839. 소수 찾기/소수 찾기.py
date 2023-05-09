from itertools import permutations
import math
def sosu(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True # 소수다

def solution(numbers):
    arr=[]
    for i in numbers:
        arr.append(i)
    per = []
    answer=0
    for i in range(1,len(arr)+1):
        per+=permutations(arr,i)
    per_list=list(set(per))

    a= []
    for per in per_list:
        a.append(int(''.join(per)))
    a=list(set(a))
    for i in a:
        if i <=1:
            continue
        if sosu(i) == True:
            print(i)
            answer+=1
    return answer