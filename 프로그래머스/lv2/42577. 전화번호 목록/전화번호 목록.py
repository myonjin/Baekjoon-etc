def solution(phone_book):
    dic={}
    for phone in phone_book:
        dic[phone] = 1
    for phone in phone_book:
        temp = ''
        for num in phone:
            temp+=num
            if temp in dic and temp != phone:
                return False
    else:
        return True
                
            
