num_01 = int(input("Enter number 1: "))
num_02 = int(input("Enter number 2: "))

if len(str(num_01)) > len(str(num_02)):
  number_of_iterating = len(str(num_02))
else:
  number_of_iterating = len(str(num_01))

counter = 0

for _ in range(number_of_iterating):
  digit_01 = num_01 % 10 
  digit_02 = num_02 % 10
  if digit_01 == digit_02:
    counter +=1
  num_01 = num_01 // 10
  num_02 = num_02 // 10
print(counter)