n = int(input("Enter the  'n': " ))
list_of_matrix = []

for _ in range(n):
  lists = input("Enter the first list items separated space:").split()
  list_of_matrix.append(lists)


summation = 0
for index in range(n):
  summation+=int(list_of_matrix[index][index])

print(summation)

  


