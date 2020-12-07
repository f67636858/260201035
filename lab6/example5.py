num = int(input("Enter the number : "))

list_of_identity_matrix=[]
counter =0
for x in range(num):
  temp_list = []
  for y in range(0,num):
    if counter == y:
      temp_list.append(1)
    else:
      temp_list.append(0)
  counter+=1
  list_of_identity_matrix.append(temp_list)

print(list_of_identity_matrix)

