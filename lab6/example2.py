grades = [[50,90,60],[15,60,75],[99,95,91]]
list_of_student_grade = []
for student_grade in grades:
  average_grade = (student_grade[0]*0.3)+(student_grade[1]*0.3)+(student_grade[2]*0.4)
  list_of_student_grade.append(average_grade)

for student_average_grade in list_of_student_grade:
  print(student_average_grade)

#example 3
for student_average_grade in list_of_student_grade:
  if student_average_grade>90:
    print(student_average_grade)
  