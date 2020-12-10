number_of_numbers = int(input("How many numbers? "))
even = 0
for _ in range(number_of_numbers):
  num = int(input("Enter an integer: "))
  if num % 2 ==0:
    even += 1

average = (even / number_of_numbers) *100
print(average ,"%")