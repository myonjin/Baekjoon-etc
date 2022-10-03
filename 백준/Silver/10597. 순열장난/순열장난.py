import sys

input = sys.stdin.readline


def makeKriii(index, c):
    global finish, ans
    if finish:
        return
    if index == len(Kriii):
        if c == maxN:
            finish = True
            ans = " ".join(map(str, tmp))
        return
    # 한자리 숫자, 두 자리 숫자 탐색

    num1 = int(Kriii[index])
    if not arr[num1]:  # 사용여부 chk
        arr[num1] = True
        tmp[c] = num1
        makeKriii(index + 1, c + 1)
        arr[num1] = False
    if index + 1 < len(Kriii):  # 두자리 숫자 chk
        num2 = int(Kriii[index:index + 2])
        if num2 < maxN + 1 and not arr[num2]:
            arr[num2] = True
            tmp[c] = num2
            makeKriii(index + 2, c + 1)
            arr[num2] = False


Kriii = input().rstrip()

if len(Kriii) < 10:
    maxN = len(Kriii)
else:
    maxN = 9 + ((len(Kriii) - 9) // 2)
arr = [0 for _ in range(maxN + 1)]
tmp = [0 for _ in range(maxN)]
finish = False
makeKriii(0, 0)
print(ans)