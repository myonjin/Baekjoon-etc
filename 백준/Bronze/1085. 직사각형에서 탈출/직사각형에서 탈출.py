x,y,w,h = map(int,input().split())
# print(x,y,w,h)
min_d=99999
if min_d>x:
    min_d=x
if min_d>w-x:
    min_d=w-x
if min_d>y:
    min_d=y
if min_d>h-y:
    min_d=h-y

print(min_d)