import sys

def inorder(arr,level):
    mid=len(arr)//2
    li[level].append(arr[mid])
    if len(arr)==1:
        return 0
    inorder(arr[:mid],level+1)
    inorder(arr[mid+1:],level+1)

K= int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
li=[[] for _ in range(K)]
inorder(arr,0)
# print(li)
for i in range(K):
    print(*li[i])
