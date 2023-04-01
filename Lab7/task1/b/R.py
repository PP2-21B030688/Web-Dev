k = int(input())
m = int(input())
n = int(input())

if n <= k:
  t = m * 2
elif (n * 2) % k == 0:
  t = m * (n * 2 // k)
else:
  t = m * (1 + (n * 2 // k))
  
print(t)