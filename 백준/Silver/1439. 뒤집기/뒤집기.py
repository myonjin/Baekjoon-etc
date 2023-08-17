# N = int(input())
# arr = list(map(int,input().split("")))
arr =input()
# print(arr)
cnt_1=0
cnt_1p=0
cnt_2=0
cnt_2p=0
for ar in arr:
    if ar == "1" and cnt_1p==0:
        cnt_1p=1
        cnt_1+=1
        cnt_2p=0
    if ar == "0" and cnt_2p==0:
        cnt_2p=1
        cnt_2+=1
        cnt_1p=0
# print(cnt_1,cnt_2)
print(min(cnt_1,cnt_2))