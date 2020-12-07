employees = {
  "Ali":2500,
  "Ahmet":3000,
  "Ayşe":2750,
  "Kadir":3750,
  "Fatih":2800,

  }

temp_dict = {}
for key,value in employees.items():
  temp_dict[value] = key

new_list = []
for key in temp_dict:
  new_list.append(key)

new_list.sort()
new_list = new_list[-3:]

for value in new_list[::-1]:
  print(temp_dict[value])


  