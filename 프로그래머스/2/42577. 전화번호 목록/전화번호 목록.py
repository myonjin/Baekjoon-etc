def solution(phone_book):
    dic = dict()
    cnt = 0
    for phone in phone_book:
        dic[phone] = cnt
        cnt+=1
    for idx,phone in enumerate(phone_book):
        for i in range(len(phone)):
            temp = phone[:(i+1)]
            if temp in dic and dic[temp] != idx:
                return False
    return True