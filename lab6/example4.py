input_user = input("Enter your number separed one space").split()
unique_number = set(input_user)
unique_number = list(unique_number)

result_list = []

for num in list(unique_number):
  temp_num = int(num)
  result_list.append(temp_num)

  

print(list(result_list))