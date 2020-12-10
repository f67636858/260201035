a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

discriminant = (b**2)-(4*a*c)
if discriminant ==0:
  print("There is one real root")
elif discriminant>0:
  print("There are two real root ")
else:
  print("There are two complex roots ")
  