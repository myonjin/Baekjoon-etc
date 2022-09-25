a=[]
for _ in range(9):
    a.append(int(input()))
print(max(a))
print(f'{a.index(max(a))+1}')