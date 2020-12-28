def hailstone(x):
  if x == 1:
    print(1)
  elif x % 2 == 0:
    print(x)
    hailstone(x // 2)
  else:
    print(x)
    hailstone(3 * x + 1)

hailstone(5)
