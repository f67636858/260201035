num_01 = int(input("Enter the number : "))
num_02 = int(input("Enter the number : "))
num_03 = int(input("Enter the number : "))

if num_01>num_02 and num_01>num_03:
  print(num_01)
elif num_02>num_01 and num_02>num_03:
  print(num_02)
else:
  print(num_03)