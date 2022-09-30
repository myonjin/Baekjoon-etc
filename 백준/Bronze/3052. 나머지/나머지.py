A=set()

while True:
    try:
        B=int(input())
        A.add(B%42)

    except:
        print(len(A))
        break