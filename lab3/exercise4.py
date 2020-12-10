age = int(input("Enter your age : "))
if age<=6 or age>=60:
  print("Free Ticket")
elif age>6 and age<=18:
  print("Ticket is 1.5 $")
else:
  print("Ticket is 3 $")
  