a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

def sum_of_list(liste):
  summation = 0
  for num in liste:
    summation += num
  return (summation) ** 2

print(round(sum_of_list(a_list),2))
