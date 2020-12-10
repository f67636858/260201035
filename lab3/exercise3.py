number_of_lectures = int(input("Enter number of lectures : "))
gpa = float(input("Enter the GPA : "))

if number_of_lectures < 47 and gpa<2.0 :
  print("Not enough number of lectures and GPA!")
elif number_of_lectures < 47 and gpa >= 2.0:
  print("Not enough number of lectures!")
elif number_of_lectures >=47 and gpa <2.0:
  print("Not enough GPA!")
else:
  print("GRADUATED!!!")

 