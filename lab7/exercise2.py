books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
result_dict = {}

index = 0
while index<len(books):
  length_of_book_name = len(books[index])
  unique_char = len(set(list(books[index])))
  result_dict[books[index]]=(length_of_book_name,unique_char)
  index+=1

for key,value in result_dict.items():
  print(f"{key}-->{value}")

for key,value in result_dict.items():
  
  average_value = int((value[0]+value[1])/2)
  value = list(value)
  value.append(average_value)
  result_value =tuple(value)
  result_dict.update({key:result_value})
print("\n")
for key,value in result_dict.items():
  print(f"{key}-->{value}")