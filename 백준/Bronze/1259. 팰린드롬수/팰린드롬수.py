while True:
    N=input()
    if N=='0':
        break
    result=''
    for i in N:
        result=i+result
    if N==result:
        print('yes')
    elif N!=result:
        print('no')