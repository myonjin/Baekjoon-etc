A,B= map(int,input().split())
s_A=''
s_B=''
for i in str(A):
    s_A=i+s_A
for i in str(B):
    s_B=i+s_B
A=int(s_A)
B=int(s_B)
if A>B:
    print(A)
else:
    print(B)