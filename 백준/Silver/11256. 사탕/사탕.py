t = int(input())
for _ in range(t) :
  j, n = map(int, input().split())

  candy = []
  for _ in range(n) :
    a, b = map(int, input().split())
    candy.append(a*b)

  candy.sort(reverse=True)
  result = 0
  for i in range(len(candy)) :
    j -= candy[i]
    result += 1
    if j <= 0 :
      break

  print(result)