number = input("Enter your number : ")
if len(number) <= 1:
  print(number)
else:
  result = int(number[-2]) + int(number[-1])
  print(result)