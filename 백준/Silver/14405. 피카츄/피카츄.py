S = input()
arr = ["pi","ka","chu"]
temp=""
for s in S:
    temp += s
    if temp in arr:
        temp = ""
        continue

    if len(temp) >= 4:
        break
if len(temp) >0:
    print("NO")
else:
    print("YES")
