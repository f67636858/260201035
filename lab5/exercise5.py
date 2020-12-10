n = 10
a = 0
b = 1
print(1, end=" ")
for _ in range(n):
  summation = a + b
  print(summation,end=" ")
  a = b
  b = summation

