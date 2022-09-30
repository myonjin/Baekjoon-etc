b = list(input().upper())
arr=list(set(b))
m=0
l=[]

for ar in list(set(arr)):
    if m < b.count(ar):
        m=b.count(ar)
        l=[]
        l.append([ar,b.count(ar)])
    elif m==b.count(ar):
        l.append([ar, b.count(ar)])


if len(l)>1:
    print('?')
else:

    print(l[0][0])