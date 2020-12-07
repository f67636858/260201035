num = int(input("Enter the number : "))

list_of_matrix = []
for _ in range(num):
  temp_list = []
  for _ in range(num):
    temp_list.append(0)
  list_of_matrix.append(temp_list)

for i in range(num):
  list_of_matrix[i][i] = 1

print(list_of_matrix)

