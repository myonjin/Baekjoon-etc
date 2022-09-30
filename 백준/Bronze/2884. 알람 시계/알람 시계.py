H,M= map(int,input().split())
M=M-45
if M<0:
    H=H-1
    M=M+60
if H<0:
    H=H+24

print(f'{H} {M}')